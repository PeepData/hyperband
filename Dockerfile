FROM python:3.8-buster

# Install compilation depedencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        default-libmysqlclient-dev libmariadbclient-dev

# Setup Tz Argentina
ENV TZ=America/Argentina/Buenos_Aires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install application into container and install python depedencies
WORKDIR /app

COPY ./requirements.txt ./
RUN python3.8 -m pip install --upgrade pip
RUN pip3.8 install -r requirements.txt

COPY . .
RUN pip3.8 install -e .
