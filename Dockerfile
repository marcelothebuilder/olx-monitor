FROM python:3.7-slim-buster
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install apt-utils build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev python-dev pipenv  -y
RUN python -m pip install --upgrade pip
RUN mkdir -p /opt/app
WORKDIR /opt/app
ADD Pipfile /opt/app
ADD Pipfile.lock /opt/app
RUN pipenv install
ADD . /opt/app
CMD pipenv run python runner.py --scheduled

