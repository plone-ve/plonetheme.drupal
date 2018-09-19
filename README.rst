=================
plonetheme.drupal
=================


Overview
========

``plonetheme.drupal`` is an installable Plone Theme using `plone.app.theming`_, 
based on the default Plone `Sunburst Theme`_.

Strongly inspired by the Drupal theme `Bartik`_ (default theme in Drupal 7), 
this theme may help sell Plone to PHP guys ;)

**To be installed before any demonstration to an audience of Drupal followers ;) !**


Requirements
============

- Tested with the following releases: *Plone 4.3 latest version*, *Plone 4.3a1*, *Plone 4.2.1.1* and *Plone 4.1.6* (https://plone.org/download).

- For Plone 4.1.6 : ``plone.app.theming`` 1.0 (please configure your buildout corresponding to `plone.app.theming 1.0 installation`_)


Screenshot
==========

.. figure:: https://github.com/sylvainb/plonetheme.drupal/raw/master/docs/plonetheme-drupal-screenshot.png
   :height: 1039px
   :width: 1026px
   :scale: 70 %
   :alt: Plone Theme Drupal Screenshot
   :align: center

  Plone Theme Drupal Screenshot


Plone versus Drupal
-------------------

Do you want to learn more about Plone versus Drupal? Install this theme and visit 

	*http://site_url/your_plone_site/@@plone-versus-drupal*

.. figure:: https://github.com/sylvainb/plonetheme.drupal/raw/master/docs/plonetheme-drupal-versus-plone.png
   :height: 1039px
   :width: 1026px
   :scale: 70 %
   :alt: Post about Plone versus Drupal Screenshot
   :align: center

  Post about Plone versus Drupal Screenshot


Installation
============


Getting the theme
-----------------

If you are a **developer user**, you might enjoy installing it via buildout.

For install ``plonetheme.drupal`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.drupal


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.drupal',
    ],

Enabling the theme
------------------

    Install the theme from the Add-ons control panel. That's it!


Quickly test?
--------------

Download plonetheme.drupal and use virtualenv and buildout to test the theme:

::

    pip install virtualenv
    cd plonetheme.drupal
    virtualenv .
    source bin/activate
    (plonetheme.drupal) pip install zc.buildout 
    !!! check the buildout config file ``test-plone-base.cfg`` before running !!!
    (plonetheme.drupal) ln -s test-plone-4.2.x.cfg buildout.cfg 
    (plonetheme.drupal) python bootstrap.py
    (plonetheme.drupal) bin/buildout
    [...] be patient... [...]
    (plonetheme.drupal) ./bin/instance fg

Go to http://localhost:8080, add a new Plone Site and install ``plonetheme.drupal`` package.

Launch tests::

    (plonetheme.drupal) ./bin/test -s plonetheme.drupal

Launch code coverage::

    (plonetheme.drupal) bin/coverage
    (plonetheme.drupal) bin/report
    And open with a browser htmlcov/index.html


Contribute
==========

- Issue Tracker: https://github.com/sylvainb/plonetheme.drupal/issues
- Source Code: https://github.com/sylvainb/plonetheme.drupal


How to contribute and submit a patch?
--------------------------------------

`Source code <https://github.com/sylvainb/plonetheme.drupal>`_ and an `issue tracker <https://github.com/sylvainb/plonetheme.drupal/issues>`_ is hosted on Github.


License
=======

This package is licensed under the GPL Version 2.


Credits
=======

- Sylvain Boureliou [sylvainb] - `GitHub <https://github.com/sylvainb>`_ - `Website <http://www.asilax.fr/>`_


Amazing contributions
---------------------

- Leonardo J. Caballero G. aka macagua (leonardocaballero at gmail dot com).

You can find an updated list of package contributors on https://github.com/sylvainb/plonetheme.drupal/contributors

.. _`Sunburst Theme`: https://github.com/plone/plonetheme.sunburst
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming
.. _`plone.app.theming 1.0 installation`: https://pypi.org/project/plone.app.theming/1.0#installation
.. _`Bartik`: https://drupal.org/documentation/themes/bartik
