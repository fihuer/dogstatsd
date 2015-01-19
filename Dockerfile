FROM debian:wheezy

MAINTAINER Romain Fihue <romain.fihue@gmail.com>

RUN apt-get update && apt-get install -qy python-pip python-dev && pip install dogstatsd-python

COPY dogstatsd.py /root/

ENTRYPOINT ./dogstatsd.py
