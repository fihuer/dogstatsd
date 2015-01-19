#!/usr/bin/python2.7
from statsd import statsd
import psutil
def setup ():
   statsd.connect('agent', 8125)
   statsd.event("Dogstats container connected !", "Running in aimnor/dogstatsd container")

def get_net_metrics():
   hash = {}
   hash.update(nb_connections())
   for name, value in hash.iteritems():
      print 'net.'+name, value
      statsd.gauge('net.'+name, value)
def nb_connections():
   conns = psutil.net_connections()
   res = {"ESTABLISHED":0, "CLOSING":0, "SYN_SENT":0, "SYN_RECV":0, "LISTEN":0, "CLOSE_WAIT":0}
   for conn in conns:
      #print conn[5]
      if conn[5] in res.keys():
         res[conn[5]] = res[conn[5]] + 1
   return res
if __name__ == "__main__":
   setup()
   get_net_metrics()



