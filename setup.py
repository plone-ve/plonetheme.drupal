import os
from setuptools import setup, find_packages

version = '1.2.dev0'

def read(*rnames):
    return open(
        os.path.join('.', *rnames)
    ).read()

long_description = "\n\n".join(
    [read('README.rst'),
     read('docs', 'HISTORY.txt'),
    ]
)

tests_require = ['zope.testing',
                 'zope.app.testing',
                 'plone.app.testing',
                 'lxml']


setup(name='plonetheme.drupal',
      version=version,
      description="Get all the power of Drupal for Plone ;)",
      long_description=long_description,
      # Get more strings from
      # https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone theme diazo web zope drupal theme',
      author='Sylvain Boureliou',
      author_email='sylvain.boureliou@gmail.com',
      maintainer='Leonardo Caballero',
      maintainer_email='leonardocaballero@gmail.com',
      url='https://github.com/sylvainb/plonetheme.drupal',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'z3c.jbot'
          # -*- Extra requirements: -*-
      ],
      tests_require=tests_require,
      test_suite='plonetheme.drupal.tests.test_docs.test_suite',
      extras_require={
        'test': tests_require,
      },
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      },
      )
