import argparse


def get_args():
    p = argparse.ArgumentParser('rconcli')

    p.add_argument('command', metavar='CMD', type=str, nargs='*')
    p.add_argument(
        '--log-level', '-l', type=int, default=20,
        help='Log Level')
    p.add_argument(
        '--silent', '-s', default=False, action='store_true',
        help='Only output command result')

    p_cred = p.add_argument_group('Credentials')
    p_cred.add_argument(
        '--properties', '-prop', type=str,
        help='Location of the server.properties')
    p_cred.add_argument(
        '--rcon-address', '-a', type=str,
        help='Address of the RCON server')
    p_cred.add_argument(
        '--rcon-password', '-p', type=str,
        help='Password of the RCON server')

    p_rcon = p.add_argument_group('RCON client')
    p_rcon.add_argument(
        '--auto-reconnect', action='store_true',
        help='Auto reconnect to RCON server on connection loss')
    p_rcon.add_argument(
        '-max-retries', type=int, default=10,
        help='Maximum ammount of command retries on failure')
    p_rcon.add_argument(
        '--rcon-encoding', type=str, default='utf-8',
        help='RCON payload encoding')

    return p.parse_args()
