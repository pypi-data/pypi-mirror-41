[![Build Status](https://travis-ci.org/kmedian/datefeatures.svg?branch=master)](https://travis-ci.org/kmedian/datefeatures)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/kmedian/datefeatures/master?urlpath=lab)

# datefeatures

## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Commands](#commands)
* [Support](#support)
* [Contributing](#contributing)


## Installation
The `datefeatures` [git repo](http://github.com/kmedian/datefeatures) is available as [PyPi package](https://pypi.org/project/datefeatures)

```
pip install datefeatures
```


## Usage
Check the [examples](examples) folder for notebooks.


## Commands
* Check syntax: `flake8 --ignore=F401`
* Run Unit Tests: `python -W ignore -m unittest discover`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`


## Support
Please [open an issue](https://github.com/kmedian/datefeatures/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/kmedian/datefeatures/compare/).
