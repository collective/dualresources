.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.dualresources
==============================================================================

An extension of the plone.resource plone:static zcml directive, that allows to specify two folders for a resource directory registration: A dev-directory and a dist-directory. When plone is running in debug mode the filesystem path specified in dev-directory is used to serve static resources for this resource registration. The dist-directory is used when not in debug mode. This allows to use tools like grunt to build production versions of resources, including minification, concatenation, image minification, etc.


Examples
========

