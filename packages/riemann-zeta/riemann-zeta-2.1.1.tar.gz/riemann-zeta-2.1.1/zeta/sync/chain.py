import asyncio

from zeta import electrum
from zeta.db import checkpoint, headers

from zeta.zeta_types import Header
from typing import cast, List, Optional, Union


async def sync(
        outq: Optional[asyncio.Queue] = None,
        network: str = 'bitcoin_main') -> None:  # pragma: nocover
    '''
    Starts all header tracking processes
    1. subscribe to headers feed (track chain tip)
    2. catch up to the servers' view of the chain tip
    3. clean up any headers that didn't fit a chain when we found them
    4. print status updates
    '''
    last_known_height = _initial_setup(network)
    # NB: assume there hasn't been a 10 block reorg
    asyncio.ensure_future(_track_chain_tip(outq))
    asyncio.ensure_future(_catch_up(last_known_height))
    asyncio.ensure_future(_maintain_db())
    # asyncio.ensure_future(_status_updater())


def _initial_setup(network: str) -> int:
    '''
    Ensures the database directory exists, and tables exist
    Then set the highest checkpoint, and return its height
    '''
    # Get the highest checkpoint
    latest_checkpoint = max(
        checkpoint.CHECKPOINTS[network],
        key=lambda k: k['height'])
    headers.store_header(latest_checkpoint)

    return cast(int, headers.find_highest()[0]['height'])


async def _track_chain_tip(
        outq: Optional[asyncio.Queue] = None) -> None:  # pragma: nocover
    '''
    subscribes to headers, and starts the header queue handler
    '''
    q: asyncio.Queue = asyncio.Queue()
    await electrum.subscribe_to_headers(q)
    asyncio.ensure_future(_header_queue_handler(q, outq))


async def _header_queue_handler(
        inq: asyncio.Queue,
        outq: Optional[asyncio.Queue] = None) -> None:
    '''
    Handles a queue of incoming headers. Ingests each individually
    Args:
        q (asyncio.Queue): the queue of headers awaiting ingestion
    '''
    while True:
        header = await inq.get()
        # NB: the initial result and subsequent notifications are inconsistent
        #     so we try to unwrap it from a list
        try:
            header_dict = header[0]
        except Exception:
            header_dict = header

        headers.store_header(header_dict['hex'])
        if outq is not None:
            await outq.put(header_dict)


async def _catch_up(from_height: int) -> None:
    '''
    Catches the chain tip up to latest by batch requesting headers
    Schedules itself at a new from_height if not complete yet
    Increments by 2014 to pad against the possibility of multiple off-by-ones
    Args:
        from_height (int): height we currently have, and want to start from
    '''
    electrum_response = await electrum.get_headers(from_height, 2016)

    # NB: we requested 2016. If we got back 2016, it's likely there are more
    if electrum_response['count'] == 2016:
        asyncio.ensure_future(_catch_up(from_height + 2014))
    _process_header_batch(electrum_response['hex'])


async def _maintain_db() -> None:
    '''
    Loop that checks the DB for headers at height 0
    Restoring them attempts to connect them to another known header
    '''
    while True:
        await asyncio.sleep(60)

        # NB: 0 means no known parent
        floating = headers.find_by_height(0)

        # NB: this will attempt to find their parent and fill in height/accdiff
        for header in floating:
            headers.store_header(header)


def _process_header_batch(electrum_hex: str) -> None:
    '''
    Processes a batch of headers and sends to the DB for storage
    Args:
        electrum_hex (str): The 'hex' attribute of electrum's getheaders res
    '''
    blob = bytes.fromhex(electrum_hex)

    # NB: this comes as a single hex string with all headers concatenated
    header_list: List[Union[Header, str]]
    header_list = [blob[i:i + 80].hex() for i in range(0, len(blob), 80)]

    headers.batch_store_header(header_list)
