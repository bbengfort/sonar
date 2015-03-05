# sonar.app
# The application that runs the Sonar ping
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Mar 05 00:24:06 2015 -0500
#
# Copyright (C) 2015 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: app.py [] benjamin@bengfort.com $

"""
The application that runs the Sonar ping.
"""

##########################################################################
## Imports
##########################################################################

from __future__ import division

import time
import requests

from dateutil.tz import tzutc
from datetime import datetime
from pymongo import MongoClient
from sonar.config import settings

##########################################################################
## Sonar Application
##########################################################################

class SonarApp(object):
    """
    Usage: instantiate this app, and then run it!
    """

    @staticmethod
    def utcnow():
        return datetime.now(tzutc())

    @staticmethod
    def milliseconds(tdelta):
        """
        Computes milliseconds from a time delta
        """
        return (tdelta.microseconds / 1000) + (tdelta.seconds * 1000) + (tdelta.days * 86400000)

    def __init__(self, **kwargs):
        """
        Accepts parameters for the app as listed in the config.py, where
        the defaults for each argument are also listed.
        """

        getarg = lambda key: kwargs.pop(key, settings.get(key, None))

        self.debug     = getarg('debug')
        self.testing   = getarg('testing')
        self.endpoints = getarg('endpoints')
        self.wait      = getarg('wait')

        dbconfig       = settings.database
        self.dbclient  = MongoClient(kwargs.get('host', dbconfig.get('host')),
                                     kwargs.get('port', dbconfig.get('port')))
        self.db        = self.dbclient[dbconfig.database]
        self.logs      = self.db[dbconfig.collection]

    def run(self):
        """
        Main method runs the pings in order, with small wait between
        """

        for endpoint in self.endpoints:

            response = requests.get(endpoint)
            result   = {
                'timestamp': self.utcnow(),
                'status_code': response.status_code,
                'elapsed': self.milliseconds(response.elapsed),
                'endpoint': endpoint,
                'method': response.request.method,
            }

            result.update(response.json())
            self.logs.insert(result)

            time.sleep(self.wait)

if __name__ == '__main__':
    app = SonarApp()
    app.run()
