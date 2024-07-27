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

RUN apt update \
    && apt install -y curl 

RUN curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash \
    &&  apt install -y speedtest

