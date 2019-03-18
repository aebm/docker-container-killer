FROM python:3.7.2-alpine3.9
MAINTAINER Alejandro Brito Monedero <alejandro.monedero@gmail.com>

WORKDIR /usr/src/app
COPY ["dc_killer.py", "test_dc_killer.py", "requirements.txt", "/usr/src/app/"]
RUN ["/usr/local/bin/pip", "install", "--requirement", "requirements.txt"]

ENTRYPOINT ["/usr/src/app/dc_killer.py"]
