Keel
====

[project] | [code] | [tracker]

A Django-based middleware application (with a user-facing web interface)
for managing services, resources and subscription-based accounts on a
Liberty Deckplan Host (LDH). The reference implementation for LDH
middleware. Tailored for services operated by Purism SPC, but ready to
be modified and deployed anywhere, by anyone.

Installation
------------

Follows an opinionated installation process (specifically expecting
one-instance-per-server), but includes a number of configuration
options.

See [SETUP.md] for prerequisites and instructions.

Usage
-----

* Start Django site as a system service, or with `./manage.py runserver`
* Visit <https://example.com> and follow the login or registration
  links.
  * If registration is closed, you will have to create LDAP credentials
    another way.
* Manage user profile at <https://example.com/accounts/profile/>

Models
------

![Database model diagram](models.png)

Model diagram generated with:

    ./manage.py graph_models --all-applications --group-models \
    --verbose-name --output models.png

Build wheel package (and optionally upload)
-------------------------------------------

Follow these instructions to build LDH as a Python package:

```
  $ apt-get install git libsasl2-dev libldap2-dev libssl-dev python3-dev virtualenv gcc python3-pip
  $ git clone https://source.puri.sm/liberty/ldh_middleware.git
  $ cd ldh_middleware
  $ pipenv install --dev
  $ pipenv shell
  $ python setup.py sdist bdist_wheel
```

If everything works as expected you should end up with the files:
* `ldh_middleware-<version>-py3-none-any.whl`
* `ldh_middleware-<version>.tar.gz`
under dist/ directory.


You can now optionally upload the created Python package to PyPI using twine:

```
  $ twine upload dist/*
```

Build Debian package
----------------------

This section details the steps that need to be taken to build a Debian
package. We used Debian Stretch to build the package but using any
other Debian based distribution should generate a valid package for
that distribution.

Install Ruby packages and configure the user environment for Ruby 2.4.0:

```
$ sudo apt-get install rbenv ruby-build
$ rbenv install 2.4.0
$ rbenv global 2.4.0
```

Install FPM gem:

```
$ rbenv exec gem install fpm
```

Install the tools needed to create a virtual environment and install
LDH from PyPI:

```
$ sudo apt-get install python3-pip virtualenv libsasl2-dev libldap2-dev libssl-dev
$ sudo pip3 install virtualenv-tools3
$ pip3 install --user setuptools
```

Now we can build a Debian package from the LDH version available in PyPI by running:

```
$ make debpypi
```

or we can build a Debian package with the sources available in our directory by running:

```
$ make debsource
```

After a successful execution you will get a `ldh-middleware_<VERSION>_amd64.deb` file.

You can use `make clean` to remove the virtual environment and the .deb file created.

Sharing and contributions
-------------------------

Keel (LDH middleware)  
<https://source.puri.sm/liberty/ldh_middleware>  
Copyright 2017-2018 Purism SPC  
SPDX-License-Identifier: AGPL-3.0-or-later

Shared under AGPL-3.0-or-later. We adhere to the Community Covenant
1.0 without modification, and certify origin per DCO 1.1 with a
signed-off-by line. Contributions under the same terms are welcome.

For details see:

* [COPYING.md], license notices
* [COPYING.AGPL.md], full license text
* [CODE_OF_CONDUCT.md], full conduct text
* [CONTRIBUTING.DCO.md], full origin text

<!-- * [CONTRIBUTING.md], additional contribution notes -->

<!-- Links -->

[project]: https://source.puri.sm/liberty/ldh_middleware
[code]: https://source.puri.sm/liberty/ldh_middleware/tree/master
[tracker]: https://source.puri.sm/liberty/ldh_middleware/issues
[SETUP.md]: SETUP.md
[COPYING.AGPL.md]: COPYING.AGPL.md
[CODE_OF_CONDUCT.md]: CODE_OF_CONDUCT.md
[CONTRIBUTING.DCO.md]: CONTRIBUTING.DCO.md
[COPYING.md]: COPYING.md
[CONTRIBUTING.md]: CONTRIBUTING.md
