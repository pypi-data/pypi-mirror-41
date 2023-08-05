import os
import asyncio
import riemann

from zeta import crypto, electrum, utils
from zeta.sync import chain, coins
from zeta.db import connection, headers  # , addresses

from typing import Any, Optional, Tuple


async def _status_updater() -> None:
    '''
    Prints stats about the heaviest (best) block every 10 seconds
    '''
    best = None
    while True:
        heaviest = headers.find_heaviest()

        # it'd be very strange if this failed
        # but I put in the check, which implies that it happened in testing
        if len(heaviest) != 0:
            if best and heaviest[0]['height'] > best['height']:
                print('chain tip advanced {} blocks'.format(
                    heaviest[0]['height'] - best['height']
                ))
            best = heaviest[0]
            print('Best Block: {} at {} with {} work'.format(
                best['hash'],
                best['height'],
                best['accumulated_work']
            ))
        await asyncio.sleep(15)


async def _report_new_headers(header_q) -> None:
    # print header hashes as they come in
    def make_block_hash(h) -> str:
        # print the header hash in a human-readable format
        return('new header: {}'.format(
            crypto.hash256(bytes.fromhex(h['hex']))[::-1].hex()))
    asyncio.ensure_future(utils.queue_printer(header_q, make_block_hash))


async def _report_new_prevouts(prevout_q) -> None:
    def humanize_prevout(prevout) -> str:
        if prevout['spent_at'] == -2:
            return('new prevout: {} sat at {} in {}...{}'.format(
                prevout['value'],
                prevout['address'][:12],
                prevout['outpoint']['tx_id'][:8],
                prevout['outpoint']['index']))
        else:
            return('spent prevout: {} sat at {} in {}...{} block {}'.format(
                prevout['value'],
                prevout['address'][:12],
                prevout['outpoint']['tx_id'][:8],
                prevout['outpoint']['index'],
                prevout['spent_at']))
    asyncio.ensure_future(utils.queue_printer(prevout_q, humanize_prevout))


async def zeta(
        header_q: Optional[asyncio.Queue] = None,
        prevout_q: Optional[asyncio.Queue] = None,
        network: str = 'bitcoin_main') -> Tuple[Any, Any]:
    '''
    Main function.
    Starts the various tasks.
    Pass in queues to access task outputs (new headers/prevout events)
    Returns references to the tasks
    '''
    # switch zeta and riemann over to whatever network we're using
    chain_name = os.environ.get('ZETA_NETWORK', network)
    riemann.select_network(chain_name)
    connection.init_conn(chain_name=chain_name)
    await electrum.electrum._make_client(chain_name)

    chain_task = asyncio.ensure_future(chain.sync(header_q, chain_name))
    coin_task = asyncio.ensure_future(coins.sync(prevout_q))

    return chain_task, coin_task


if __name__ == '__main__':
    # start tracking
    header_q: asyncio.Queue = asyncio.Queue()
    prevout_q: asyncio.Queue = asyncio.Queue()

    # store the sample address
    chain_name = os.environ.get('ZETA_NETWORK', 'bitcoin_main')
    riemann.select_network(chain_name)
    connection.init_conn(chain_name=chain_name)

    # DEBUG CODE
    # addresses.store_address('tb1qk0mul90y844ekgqpan8mg9lljasd59ny99ata4')

    asyncio.ensure_future(zeta(header_q, prevout_q, chain_name))

    # wait a few seconds then start the status updater
    asyncio.ensure_future(_status_updater())
    asyncio.ensure_future(_report_new_headers(header_q))
    asyncio.ensure_future(_report_new_prevouts(prevout_q))

    asyncio.get_event_loop().run_forever()
