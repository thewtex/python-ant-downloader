#!/usr/bin/python

import gant
import logging
import sys
import time

logging.basicConfig(level=logging.DEBUG, out=sys.stderr, format="%(asctime)s %(levelname)s %(message)s")

device = gant.GarminAntDevice()
net = device.claim_network()
chan = device.claim_channel()
for n in range(0, 10):
	net.network_key = "\xa8\xa4\x23\xb9\xf5\x5e\x63\xc1"
	chan.network = net
	chan.channel_type = 0x00
	chan.period = 0x1000
	chan.search_timeout = 0xff
	chan.rf_freq = 0x32
	chan.device_type = 0x00
	chan.trans_type = 0x00
	chan.open()
	for n in range(0, 100):
		print chan.get_channel_status()
		print chan.get_channel_id()
	chan.close()

# vim et ts=4 sts=8