> ## Outdated!
> This repository is sort of outdated and has some bugs. Please use the following RCON client implementation: [**zekroTJA/rconcli**](https://github.com/zekrotja/rconcli).

# rconclient

A simple staight forward RCON client especially concipated to be used in Docker containers.

> If you are interested in the RCON implementation, take a look [**here**](https://github.com/zekroTJA/asyncrcon). This project is using the package [`asyncrcon`](https://pypi.org/project/asyncrcon) for that.

## Usage

```
usage: rconcli [-h] [--log-level LOG_LEVEL] [--silent] [--version] 
               [--properties PROPERTIES] [--rcon-address RCON_ADDRESS] 
               [--rcon-password RCON_PASSWORD] [--auto-reconnect] 
               [-max-retries MAX_RETRIES] [--rcon-encoding RCON_ENCODING]
               [CMD [CMD ...]]

positional arguments:
  CMD

optional arguments:
  -h, --help            show this help message and exit
  --log-level LOG_LEVEL, -l LOG_LEVEL
                        Log Level
  --silent, -s          Only output command result
  --version, -v         Dispaly version information

Credentials:
  --properties PROPERTIES, -prop PROPERTIES
                        Location of the server.properties
  --rcon-address RCON_ADDRESS, -a RCON_ADDRESS
                        Address of the RCON server
  --rcon-password RCON_PASSWORD, -p RCON_PASSWORD
                        Password of the RCON server

RCON client:
  --auto-reconnect      Auto reconnect to RCON server on connection loss
  -max-retries MAX_RETRIES
                        Maximum ammount of command retries on failure
  --rcon-encoding RCON_ENCODING
                        RCON payload encoding
```

## Installation

If you want to use a single binary instead of executing the script, use the `Makefile` do build the binary:
```
$ make
```

If you are using Linux, you can then use the following command to install the binary to `/usr/bin/rconclient`.
```
$ make install
```

## Ship with Docker

Best practice is to use a staged docker image with the first stage using an `python:3` image to build the binary and then copying the binary into the final image:

```Dockerfile
FROM python:3.7-stretch as build

WORKDIR /build/rcon

RUN git clone https://github.com/zekroTJA/rconclient \
      --branch master --depth 1 .
RUN python3 -m pip install -r requirements.txt &&\
    python3 -m pip install pyinstaller
RUN pyinstaller rconclient/main.py --onefile


FROM openjdk:11.0.3-jdk-stretch as final

COPY --from=build /build/rcon/dist/main /usr/bin/rconcli
RUN chmod +x /usr/bin/rconcli
```

[**Here**](https://github.com/zekroTJA/spigot-autobuild/blob/master/Dockerfile) you can find a full Dockerfile where this configuration is used.

---

© 2020 Ringo Hoffmann (zekro Development)  
Covered by the MIT Licence.
