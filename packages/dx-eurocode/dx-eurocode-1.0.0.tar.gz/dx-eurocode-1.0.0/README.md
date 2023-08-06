# `dx-eurocode`

A base package for structural design with [EN Eurocodes][EC].

# Installation

## Development

This repository includes nested submodules. Thus it has to be cloned with the
appropriate options for initializing and cloning the submodules. For more
information on working with submodules see the relevant discussion
[here][nested-submodules] and the reference on [Pro Git][pro-git-submodules].

* Clone the repository

        $ git clone --recurse-submodules git@gitlab.com:d-e/dx-eurocode.git [local-path]

* Create virtual environment:

        $ make install

* Activate virtual environment and run tests:

        $ source venv/bin/activate
        $ nose2

## As a dependency

### From source code

```
$ pip install git://git@gitlab.com/d-e/dx-eurocode.git#egg=dx_eurocode
```

### From Python Package Index (PyPI)

```
$ pip install dx-eurocode
```

## Features

* Eurocode, Part 0 ([EC0][])

  * Safety factors

* Eurocode, Part 2 ([EC2][])

  * Materials
  * Recurrent formulas
  * Safety factors

### Sample usage

```
>>> from dx_eurocode.EC2.materials import RC
>>> C16_20 = RC[16] # RC['16'] works as well!
>>> C16_20.fck
16000000.0
>>> C16_20.fcm
24000000.0
>>> C16_20.Ecm
28607904894.961403
>>> C16_20.gamma
{'accidental': {'ultimate': 1.2},
 'persistent': {'ultimate': 1.5},
 'transient': {'ultimate': 1.5}}
>>> C16_20.fcd(design_situation='persistent', limit_state='ultimate')
10666666.666666666
```

## Contribute

Source code lives in https://gitlab.com/d-e/dx-eurocode.

### Code of conduct

We abide by the provisions of [Contributor Coventant Code of Conduct][COC].

### Workflow

Follow this [simplified gitflow model][gitflow].

### Coding standards

* Follow [PEP8 rules](https://www.python.org/dev/peps/pep-0008/).
* Populate docstrings with concise descriptions and the signature
  of the object according to [sphinx guidelines][sphinx-sig]. For a
  complete overview of documentation options see
  [Sphinx docs](http://www.sphinx-doc.org)
* Write unit-tests.

### Versioning

We follow [semantic versioning][semver].

### Review the docs locally

Documentation is generated through continuous-integration (CI). For
review purposes it can be generated locally with:

```
$ make MODPATH=../dx_eurocode -C docs apidoc html
```

For more details on the process run

```
$ make docs-help
```

## Public API

See the [documentation pages](https://d-e.gitlab.io/dx-eurocode/).

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the [GNU Affero General Public License](LICENSE) as
published by the Free Software Foundation, either version 3 of the
License, or any later version.

[EC]: https://eurocodes.jrc.ec.europa.eu/
[EC0]: https://eurocodes.jrc.ec.europa.eu/showpage.php?id=130
[EC2]: https://eurocodes.jrc.ec.europa.eu/showpage.php?id=132
[gitflow]: https://gitlab.com/d-e/dx-utilities/wikis/git-workflow
[semver]: https://semver.org/
[COC]: https://www.contributor-covenant.org/version/1/4/code-of-conduct
[sphinx-sig]: http://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#info-field-lists
[nested-submodules]: http://social.d-e.gr/techblog/posts/10-python-projects-with-git-submodules
[pro-git-submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
