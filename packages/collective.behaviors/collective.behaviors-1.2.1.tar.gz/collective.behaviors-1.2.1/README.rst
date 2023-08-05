.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.behaviors
==============================================================================

Adds the following behaviors to your content type:

- Organisation Structure
- Event Speakers to the Event Content-Type
- Event Sponsors to the Event Content-Type
- Allow the title of aq_parent as a creator for the Content-Type.

In addition, it adds additional catalogs and indexers for each behavior.

Features
------------

- collective.behaviors.events
- collective.behaviors.organisation
- collective.behaviors.vocabularies.IParentTitleAsCreator

Installation
------------

Install collective.behaviors by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.behaviors


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.behaviors/issues
- Source Code: https://github.com/collective/collective.behaviors

License
-------

The project is licensed under the GPLv2.
