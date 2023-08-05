# Rokit: Redirection Optimization Kit

[![PyPI version](https://badge.fury.io/py/rokit.svg)](https://badge.fury.io/py/rokit)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.com/wizardbyron/rokit.svg?branch=master)](https://travis-ci.com/wizardbyron/rokit)
[![codecov](https://codecov.io/gh/wizardbyron/rokit/branch/master/graph/badge.svg)](https://codecov.io/gh/wizardbyron/rokit)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/85709197d31d4fa3b923e5c885523147)](https://www.codacy.com/app/wizardbyron/rokit?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wizardbyron/rokit&amp;utm_campaign=Badge_Grade)
![Python versions](https://img.shields.io/pypi/pyversions/rokit.svg)

**Rokit** (Redirection Optimization Kit) is a CLI tool to help wed admin/developer to test or optimize URL redirection. It's easy to integrate into your CI as smoke test and regression test for redirection testing.

![Usage](https://wizardbyron.github.io/images/rokit/usage.svg)

## Installation

Install via pip:

```shell
pip install rokit
```

## Usage

Get a redirection chain:

```shell
$ rokit http://www.github.com
Redirect 2 time(s): http://www.github.com -> https://www.github.com/ -> https://github.com/
```

Verify if a url is in redirection chain:

```shell
$ rokit http://www.github.com https://www.github.com
Redirect 2 time(s): http://www.github.com -> https://www.github.com/ -> [https://github.com/]
[PASS] Request to http://www.github.com will  redirect to https://github.com/
```

## License

[License](LICENSE)