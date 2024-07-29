### DESCRIPTION
# Docker file to create Docker image for Internet Speed test exporter.

### INPUTS
#

### CHANGE LOG
# Author:   Stanisław Horna
# GitHub Repository:  https://github.com/StanislawHornaGitHub/Internet_SpeedTest_exporter
# Created:  27-Jul-2024
# Version:  1.0

# Date            Who                     What
#

FROM ubuntu:22.04

ENV SPEED_TEST_INTERVAL_MINUTES="60"
ENV API_PORT="8000"
ENV INTERFACE_IP="0.0.0.0"
ENV TZ="Europe/Warsaw"

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata

RUN apt update \
    && apt install -y curl python3-dev pip

RUN curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash \
    &&  apt install -y speedtest

COPY ./app /app

WORKDIR /app

RUN pip install -r ./requirements.txt

CMD [ "python3", "-u", "./main.py" ]