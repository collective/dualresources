# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.dualresources


class CollectiveDualresourcesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.dualresources)

    def setUpPloneSite(self, portal):
        pass


COLLECTIVE_DUALRESOURCES_FIXTURE = CollectiveDualresourcesLayer()


COLLECTIVE_DUALRESOURCES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_DUALRESOURCES_FIXTURE,),
    name='CollectiveDualresourcesLayer:IntegrationTesting'
)


COLLECTIVE_DUALRESOURCES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_DUALRESOURCES_FIXTURE,),
    name='CollectiveDualresourcesLayer:FunctionalTesting'
)


COLLECTIVE_DUALRESOURCES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_DUALRESOURCES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveDualresourcesLayer:AcceptanceTesting'
)
