import os

from App.config import getConfiguration
from zope.interface import Interface
from zope.component.zcml import handler
from zope.configuration.exceptions import ConfigurationError
from zope.configuration.fields import PythonIdentifier
from zope.schema import ASCIILine, TextLine

from plone.resource.interfaces import IResourceDirectory
from plone.resource.directory import FilesystemResourceDirectory


class IDualResourceDirectoryDirective(Interface):
    """Register resource directories with the global registry.
    """

    dev_directory = TextLine(
        title=u'Development directory path',
        description=u'Path relative to the package.',
        required=True
        )

    dist_directory = TextLine(
        title=u'Distribution/production directory path',
        description=u'Path relative to the package.',
        required=True
        )

    name = PythonIdentifier(
        title=u'Name',
        description=u'Name of the directory. If not specified, the name of '
                    u'the current package is used.',
        required=False,
        )

    type = ASCIILine(
        title=u'Resource type',
        required=False,
        )


def registerDualResourceDirectory(_context,
                                  dev_directory,
                                  dist_directory,
                                  name=None,
                                  type=None):
    """
    Register a new resource directory.

    The actual ZCA registrations are deferred so that conflicts can be resolved
    via zope.configuration's discriminator machinery.
    """

    if _context.package and os.path.isabs(dev_directory):
        raise ConfigurationError('Resource directories in distributions must '
                                 'be specified as relative paths.')
    elif _context.package:
        dev_directory = _context.path(dev_directory)
    elif not _context.package and not os.path.isabs(dev_directory):
        raise ConfigurationError('Global resource directories must be '
                                 'specified as absolute paths.')

    if _context.package and os.path.isabs(dist_directory):
        raise ConfigurationError('Resource directories in distributions must '
                                 'be specified as relative paths.')
    elif _context.package:
        dist_directory = _context.path(dist_directory)
    elif not _context.package and not os.path.isabs(dist_directory):
        raise ConfigurationError('Global resource directories must be '
                                 'specified as absolute paths.')

    # TODO: make sure this works in Windows
    if '..' in dev_directory.split('/'):
        raise ConfigurationError('Traversing to parent directories '
                                 'via .. is not allowed.')
    if not os.path.exists(dev_directory):
        raise IOError('Directory not found: %s' % dev_directory)

    if '..' in dist_directory.split('/'):
        raise ConfigurationError('Traversing to parent directories '
                                 'via .. is not allowed.')
    if not os.path.exists(dist_directory):
        raise IOError('Directory not found: %s' % dist_directory)

    if name is None and _context.package:
        name = _context.package.__name__

    if type:
        identifier = '++%s++%s' % (type, name or '')
    else:
        if _context.package:
            raise ConfigurationError('Resource directories in distributions '
                                     'must have a specified resource type.')
        identifier = name or ''

    zconfig = getConfiguration()
    debug_mode = zconfig.debug_mode
    if debug_mode or 'THEME_USE_DEV_DIRECTORY' in os.environ:
        directory = os.path.sep.join(dev_directory.split('/'))
    else:
        directory = os.path.sep.join(dist_directory.split('/'))
    directory = FilesystemResourceDirectory(directory, name)

    _context.action(
        discriminator=('plone:dualstatic', identifier),
        callable=handler,
        args=('registerUtility', directory, IResourceDirectory, identifier),
        )
