# tests
# Test package for the Sonar app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Mar 05 00:01:36 2015 -0500
#
# Copyright (C) 2015 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Test package for the Sonar app
"""

##########################################################################
## Imports
##########################################################################

import unittest

##########################################################################
## Fixtures
##########################################################################

__version__ = "0.1b1"

##########################################################################
## Initialization Tests
##########################################################################

class InitializationTests(unittest.TestCase):

    def test_sanity(self):
        """
        Assert the world is sane and 5+8=13
        """
        self.assertEqual(5+8, 13)

    def test_import(self):
        """
        Check that we can import the library
        """
        try:
            import sonar
        except ImportError:
            self.fail("Could not import sonar!")

    def test_version(self):
        """
        Ensure the test version matches sonar version
        """
        import sonar
        self.assertEqual(sonar.get_version(), __version__)
