======
|logo|
======

|release| |coverage|

.. |logo| image:: https://bitbucket.org/fluiddyn/fluiddevops/raw/default/doc/logo.svg
   :alt: FluidDevOps

.. |release| image:: https://img.shields.io/pypi/v/fluiddevops.svg
   :target: https://pypi.python.org/pypi/fluiddevops/
   :alt: Latest version

.. |coverage| image:: https://codecov.io/bb/fluiddyn/fluiddevops/branch/default/graph/badge.svg
  :target: https://codecov.io/bb/fluiddyn/fluiddevops

FluidDevOps is a small package which provides some console scripts to
make DevOps easier.

See directory ``docker`` for more on running Docker containers.

Installation
------------

::

    python setup.py develop

Features
--------

- ``fluidmirror`` or ``fm``  to easily setup
  mercurial and git mirroring for a group of packages and periodically check
  for updates::

    basic commands:

        init             initialize mirror.cfg
        list             list configuration
        clone            hg clone
        set-remote       set remote (push) path in hgrc
        pull             hg pull -u
        push             hg push
        sync             sync: pull and push
        run              run a shell command inside the repo(s)


- ``fluidicat`` to display the output of a command or contents of a file
  intermittently::

    positional arguments:
      FILE                  Files to read, if empty, stdin is used
    optional arguments:
      -h, --help            show this help message and exit
      -e EVERY, --every EVERY
                            Print every N line
      -w WAIT, --wait WAIT  Wait time before displaying a message

- ``bitbucket`` or ``bb`` to interact with Bitbucket::

    basic commands:

        init             initialize bitbucket configuration file
        create           create a new bitbucket repository
        update           update an existing bitbucket repository
        delete           delete an existing bitbucket repository
        clone            clone a bitbucket repository
        pull             pull a bitbucket repository
        create_from_local
                         create a bitbucket repo from existing local repo
        pull_request     open a bitbucket pull request
        download         download a file from a bitbucket repo
        list             list all bitbucket repos
        privilege        update account privilege on an existing repo
        group-privilege  update group privilege on an existing repo
        add_remote       add remote url

    See `bitbucket <command> --help` for more information on a specific command.
