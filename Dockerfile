FROM debian:wheezy

MAINTAINER Romain Fihue <romain.fihue@gmail.com>

RUN apt-get update && apt-get install python-pip python-dev && pip install dogstatsd-python
