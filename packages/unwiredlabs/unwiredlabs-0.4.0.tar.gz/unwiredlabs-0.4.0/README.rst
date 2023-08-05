Unwiredlabs Location API client for python
==========================================

This implements the Unwiredlabs Location API protocol in python

Installation
------------

Just install with ``pip``::

	pip install unwiredlabs

Usage
-----

Python example::

	import unwiredlabs

	key = 'ABCDEF1234567890'  # from the API console

	bssid = 'ab:cd:ef:12:34:56'
	rssi = -60

	request = unwiredlabs.UnwiredRequest()
	request.addAccessPoint(bssid, rssi)

	connection = unwiredlabs.UnwiredConnection(key=key)
	response = connection.performRequest(request)

	if response.status != 'Ok':
		print('Error:', response.status)
	else:
		print('Response: ', response.coordinate)

Command line client
-------------------

In the ``test`` directory you'll find a command line client to test if everything works::

	$ python cmdline_client.py --help
	usage: cmdline_client.py [-h] -k KEY [-w WIFI] [-g GPS] [-c CELL]
							 [-l LTE] [-u UMTS] [-m CDMA] [-a]

	Make a location request against the unwiredlabs location API

	optional arguments:
	  -h, --help            show this help message and exit
	  -k KEY, --key KEY     token from Unwired API panel
	  -w WIFI, --wifi WIFI  WIFI BSSID and signal strength (format: XX:XX:XX:XX:XX:XX@RSSI)
	  -g GPS, --gps GPS     GPS coordinate (format: latitude,longitude@num_satelites)
	  -c CELL, --cell CELL, --celltower CELL
							GSM Celltower information (format: MCC,MNC,LAC,CellID@RSSI)
	  -l LTE, --lte LTE     LTE Celltower information (format: MCC,MNC,LAC,CellID@RSSI)
	  -u UMTS, --umts UMTS  UMTS (3G) Celltower information (format: MCC,MNC,LAC,CellID@RSSI)
	  -m CDMA, --cdma CDMA  CDMA/EVDO Celltower information (format: MCC,MNC,LAC,CellID@RSSI)
	  -a, --address         Fetch address info in addition to coordinates
