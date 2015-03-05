# sonar.config
# Loads configuration from YAML file
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Mar 05 00:15:06 2015 -0500
#
# Copyright (C) 2015c Bengfort.com
# For license information, see LICENSE.txt
#
# ID: config.py [] benjamin@bengfort.com $

"""
Loads configuration from YAML file
"""

##########################################################################
## Imports
##########################################################################

import os

from confire import Configuration

##########################################################################
## Database Configuration
##########################################################################

class DatabaseConfiguration(Configuration):
    """
    This object contains the default connections to a MongoDB.
    """

    host            = "localhost"
    port            = 27017
    database        = "sonar"

##########################################################################
## Sonar Configuration Defaults
##########################################################################

class SonarConfiguration(Configuration):
    """
    Configuration required by the Sonar app.
    """

    CONF_PATHS = [
        '/etc/sonar.yaml',                    # The global configuration
        os.path.expanduser('~/.sonar.yaml'),  # User specific configuration
        os.path.abspath('conf/sonar.yaml'),   # Local directory configuration
    ]

    debug           = True                    # Are we in debug mode?
    testing         = False                   # Are we in testing mode?
    database        = DatabaseConfiguration() # The database configuration
    endpoints       = []                      # Endpoints to ping

##########################################################################
## Import this loaded Configuration
##########################################################################

settings = SonarConfiguration.load()

if __name__ == '__main__':
    print settings
