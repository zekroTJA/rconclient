import logging
from os import path


class Properties:

    address: str
    password: str
    rcon_enabled: bool

    _logger: logging.Logger

    def __init__(self, argv):
        self._logger = logging.getLogger('PROPERTIES')
        self.rcon_enabled = True
        self.address = argv.rcon_address or 'localhost:25575'
        self.password = argv.rcon_password
        self._load_from_file(argv.properties)
        self._check()

    def _load_from_file(self, floc: str):
        if not floc or not path.isfile(floc):
            self._logger.error('properties file not found: \'{}\''.format(floc))
            return

        self._logger.info('getting config from properties file')
        prop = {}
        with open(floc) as f:
            for line in f:
                line = line.strip().replace('\n', '')
                if len(line) == 0 or line.startswith('#'):
                    continue
                line_split = line.split('=')
                if len(line_split) < 2:
                    continue
                prop[line_split[0]] = line_split[1]

        self.rcon_enabled = prop.get('enable-rcon') == 'true'

        ip = prop.get('server-ip') or 'localhost'
        port = prop.get('rcon.port') or '25575'

        self.address = '{}:{}'.format(ip, port)
        self.password = prop.get('rcon.password') or self.password

    def _check(self):
        if not self.rcon_enabled:
            self._logger.critical('RCON is disabled in server.properties')
            exit()
        if not self.password:
            self._logger.critical('no RCON password provided')
            exit()
