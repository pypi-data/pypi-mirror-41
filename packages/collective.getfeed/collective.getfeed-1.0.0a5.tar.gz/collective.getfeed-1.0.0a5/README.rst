.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.getfeed
==============================================================================

.. image:: https://raw.github.com/collective/collective.getfeed/master/docs/forContent.png
   :alt: forContent
   :target: https://www.forcontent.com.br/


.. image:: https://secure.travis-ci.org/collective/collective.getfeed.png
    :target: http://travis-ci.org/collective/collective.getfeed

Integrate Plone with other websites through feeds.

Development
-----------

Requirements:

- Python 2.7
- Virtualenv

Setup::

  make

Run Static Code Analysis::

  make code-Analysis

Run Unit / Integration Tests::

  make test

Run Robot Framework based acceptance tests::

  make test-acceptance

Installation
-------------

To enable this product in a buildout-based installation:

#. Edit your buildout.cfg and add ``collective.getfeed`` to the list of eggs to install::

    [buildout]
    ...
    eggs =
        collective.getfeed

After updating the configuration you need to run ''bin/buildout'', which will take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``collective.getfeed`` and click the 'Activate' button.

Configuration
-------------

Add a new instance to be called with clock-server to update all feeds automatically:

.. code-block:: ini

    [buildout]
    parts +=
        instance-feeds

    [instance-feeds]
    <=instance
    port-base = 8
    zodb-cache-size = 5000
    zope-conf-additional =
        <clock-server>
           method /@@get-all-feeds
           period 3600
           user feed_user
           password feed_password
           host localhost:8088
        </clock-server>

Credits
-------

* This project icon uses The Font Awesome pictograms are licensed under the CC BY 3.0 License https://creativecommons.org/licenses/by/3.0/
