```nohighlight
\
/    /\__/\
\__=(  o_O )=
(__________)
 |_ |_ |_ |_
```

[![builds.sr.ht status](https://builds.sr.ht/~adqm/catsoop.svg)](https://builds.sr.ht/~adqm/catsoop?)
[![PyPI: Latest Version](https://img.shields.io/pypi/v/catsoop.svg)](https://pypi.org/project/catsoop/)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/catsoop.svg)
[![License: AGPLv3+](https://img.shields.io/pypi/l/catsoop.svg)](https://hz.mit.edu/git/catsoop/catsoop/raw/branch/master/LICENSE)
# CAT-SOOP

* Web Site: https://catsoop.mit.edu

* Clone Repository: `git clone https://git.sr.ht/~adqm/catsoop`

* Repository Web Access: <https://git.sr.ht/~adqm/catsoop>

* Bug Tracker: <https://todo.sr.ht/~adqm/catsoop>

* IRC: `#catsoop` on OFTC (`irc.oftc.net`)

* Mailing Lists:

    * `~adqm/catsoop@lists.sr.ht` for general-purpose discussion, questions, feedback ([archives/subscribe](https://lists.sr.ht/~adqm/catsoop))
    * `~adqm/catsoop-announce@lists.sr.ht`, low volume list for announcing new versions, features, etc ([archives/subscribe](https://lists.sr.ht/~adqm/catsoop-announce))
    * `~adqm/catsoop-dev@lists.sr.ht` for development-related discussion, including patch submission ([archives/subscribe](https://lists.sr.ht/~adqm/catsoop-dev))


## WHAT IS IT?

CAT-SOOP is a tool for automatic collection and assessment of online exercises, originally developed primarily for use in MIT's 6.01 (Introduction to Electrical Engineering and Computer Science via Robotics).

CAT-SOOP is free/libre software, available under the terms of the [GNU Affero General Public License, version 3+](https://www.gnu.org/licenses/agpl-3.0.en.html).  Please note that the terms of this license apply to the CAT-SOOP system itself and any plugins in use, but not to any course material hosted on a CAT-SOOP instance, unless explicitly stated otherwise.


## HOW DO I INSTALL IT?

To install, run:

```nohighlight
pip3 setup.py install
```

Or, from a clone of the repository, run:

```nohighlight
python setup.py install
```

#### Configuring

To generate a config.py file, run:

```nohighlight
catsoop configure
```

If you are setting up a public-facing copy of CAT-SOOP (as opposed to a local copy for debugging purposes), see the instructions at https://catsoop.mit.edu/website/docs/installing/server_configuration

#### Running

To start the server, run:

```nohighlight
catsoop runserver
```

#### Testing

To run all the unit tests:

```nohighlight
python setup.py test
```


## IS IT ANY GOOD?

Yes.


## INCLUDED SOFTWARE

CAT-SOOP incorporates pieces of third-party software.  Licensing information for the original programs is available in the `LICENSE.included_software` file.  The CAT-SOOP distribution also includes several pieces of third-party software.  Licensing information for these programs is included in this distribution, in the `LICENSE.bundled_software` file.
