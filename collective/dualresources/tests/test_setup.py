# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.dualresources.testing import COLLECTIVE_DUALRESOURCES_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.dualresources is properly installed."""

    layer = COLLECTIVE_DUALRESOURCES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
