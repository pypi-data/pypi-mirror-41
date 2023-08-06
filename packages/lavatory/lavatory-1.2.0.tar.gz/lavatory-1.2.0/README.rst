|Build Status| |Doc Status| |PyPi Badge|


Lavatory
========

Tooling to define repository specific retention policies in Artifactory.
Allows highly customizable retention policies via Python plugins.

See `Lavatory Documentation`_ for the full docs. 

Requirements
------------

-  Python 3.4+
-  Artifactory user with API permissions

Authentication
--------------

This tool looks for 3 enviroment variables in order to authenticate:

``ARTIFACTORY_URL`` - Base URL to use for Artifactory connections

``ARTIFACTORY_USERNAME`` - Username to Artifactory

``ARTIFACTORY_PASSWORD`` - Password for Artifactory

These will be loaded in at the beginning of a run and raise an exception
if missing.

Installing
----------

From pypi:

``pip install lavatory``

Or install directly from the code:

::

    git clone https://github.com/gogoair/lavatory
    cd lavatory
    pip install -U .

Running
-------

::

    $ lavatory --help
    Usage: lavatory [OPTIONS] COMMAND [ARGS]...

      Lavatory is a tool for managing Artifactory Retention Policies.

    Options:
      -v, --verbose  Increases logging level.
      --help         Show this message and exit.

    Commands:
      purge  Deletes artifacts based on retention policies.
      stats    Get statistics of a repo.
      version  Print version information.

Purging Artifacts
~~~~~~~~~~~~~~~~~

``lavatory purge --policies-path=/path/to/policies``

::

    $ lavatory purge --help
    Usage: lavatory purge [OPTIONS]

      Deletes artifacts based on retention policies.

    Options:
      --policies-path TEXT            Path to extra policies directory.
      --dryrun / --nodryrun           Dryrun does not delete any artifacts.
                                      [default: True]
      --default / --no-default        Applies default retention policy.  [default:
                                      True]
      --repo TEXT                     Name of specific repository to run against.
                                      Can use --repo multiple times. If not
                                      provided, uses all repos.
      --repo-type [local|virtual|cache|any]
                                      The types of repositories to search for.
                                      [default: local]
      --help                          Show this message and exit.


If you want to run Lavatory against a specific repository, you can use ``--repo <repo_name>``.
You can specify ``--repo`` as multiple times to run against multiple repos. If ``--repo`` is not
provided, Lavatory will run against all repos in Artifactory.  

Getting Statistics
~~~~~~~~~~~~~~~~~~
``lavatory stats --repo test-local``

::

    $ lavatory stats --help
    Usage: lavatory stats [OPTIONS]

      Get statistics of a repo.

    Options:
      --repo TEXT               Name of specific repository to run against. Can
                                use --repo multiple times. If not provided, uses
                                all repos.
      --help       Show this message and exit.

Policies
--------

See the `Creating Retention Policies`_ docs for more details on how
to create and use retention policies with Lavatory.

Listing Policies
~~~~~~~~~~~~~~~~

Lavatory looks at a policy functions docstring in order to get a description. You can list all repos and a description
of the policy that would apply to them with the ``lavatory policies`` command.

::

    $ lavatory policies --help
    Usage: lavatory policies [OPTIONS]

      Prints out a JSON list of all repos and policy descriptions.

    Options:
      --policies-path TEXT            Path to extra policies directory.
      --repo TEXT                     Name of specific repository to run against.
                                      Can use --repo multiple times. If not
                                      provided, uses all repos.
      --repo-type [local|virtual|cache|any]
                                      The types of repositories to search for.
                                      [default: local]
      --help                          Show this message and exit.

Testing
-------

::

    pip install -r requirements-dev.txt
    tox

.. |Build Status| image:: https://travis-ci.org/gogoair/lavatory.svg?branch=master
   :target: https://travis-ci.org/gogoair/lavatory

.. |Doc Status| image:: https://readthedocs.org/projects/lavatory/badge/?version=latest
   :target: http://lavatory.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status   

.. |PyPi Badge| image:: https://badge.fury.io/py/lavatory.svg
    :target: https://badge.fury.io/py/lavatory

.. _`Lavatory Documentation`: http://lavatory.readthedocs.io/en/latest/index.html  
.. _`Creating Retention Policies`: http://lavatory.readthedocs.io/en/latest/policies/index.html