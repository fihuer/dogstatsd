#!/usr/bin/python2.7
from statsd import statsd

def setup ():
   statsd.connect('agent', 8125)
   statsd.event("Dogstats container connected !", "Running in aimnor/dogstatsd container")

if __name__ == "__main__":
   setup()




