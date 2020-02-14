import args
import logging
import asyncio
from prop import Properties
from asyncrcon import AsyncRCON, AuthenticationException


def main():
    argv = args.get_args()

    logging.basicConfig(
        level=60 if argv.silent else argv.log_level,
        format='%(levelname)s | %(name)s | %(message)s')

    prop = Properties(argv)

    rcon = AsyncRCON(prop.address, prop.password,
                     max_command_retries=argv.max_retries,
                     auto_reconnect=argv.auto_reconnect)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(routine(rcon, argv, prop))
    rcon.close()
    loop.close()


async def routine(rcon: AsyncRCON, argv, prop: Properties):
    logger = logging.getLogger('ROUTINE')
    try:
        await rcon.open_connection()
    except AuthenticationException:
        logger.fatal('Connection failed: Unauthorized.')
        return
    logger.info('Connected to {}'.format(prop.address))

    if argv.command:
        cmd = ' '.join(argv.command)
        logger.info('CMD: {}'.format(cmd))
        await exec_command(rcon, cmd)
        return

    logger.info('Enter \'quit\' or \'q\' to exit')
    while True:
        inpt = input('> ')
        if inpt in ['q', 'quit', 'exit', 'e', 'close']:
            logger.info('Closing')
            return
        await exec_command(rcon, inpt)


async def exec_command(rcon: AsyncRCON, cmd: str):
    print(await rcon.command(cmd))


if __name__ == '__main__':
    main()
