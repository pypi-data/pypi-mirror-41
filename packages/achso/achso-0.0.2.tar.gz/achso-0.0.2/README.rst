=====
AchSo
=====

This is the backend implementation of AchSo: AtCoder Helper Suite.
This software offers several functionalities to manipulate `AtCoder <https://atcoder.jp/>`_ from command-line, and particularly meant to be used through editor/IDE frontends.
Currently we have frontend implementations for the following editors.

* `GNU Emacs <https://github.com/kissge/achso-emacs>`_

Supported Python versions are Python 2.7+ and Python 3.4+, but probably AchSo works well with older versions, which I haven't tested.

Installation
------------

The easiest way to install the package is via ``pip``::

    $ pip install achso

Then put your configuration file to ``${HOME}/.achso.conf``.
Below is an example::

    {
        "credentials": {
            "id": "<your AtCoder ID>",
            "password": "<your AtCoder password>"
        },
        "sample": {
            "filename": "%inout%-%id%-%number%.txt"
        }
    }

You can confirm whether the installation and the configuration are successful, by running this::

    $ achso tasks practice
    {"error": false, "tasks": [{"slug": "practice_1", "id": "A", "title": "\u306f\u3058\u3081\u3066\u306e\u3042\u3063\u3068\u3053\u30fc\u3060\u30fc\uff08Welcome to AtCoder\uff09", "time_limit": "2 sec", "memory_limit": "256 MB", "internal_id": "207"}]}

For further instructions about the commands, see ``achso -h``.

Developing AchSo
----------------

If you want to develop AchSo, a typical workflow should be something like:

* Clone this repository.
* Set up ``virtualenv`` if you want.
* Run ``pip install -e .``.
* Write your code.

Copyright and License
---------------------

This software is licensed under the MIT License (X11 License).

Copyright (C) 2016 Yuto Kisuge
