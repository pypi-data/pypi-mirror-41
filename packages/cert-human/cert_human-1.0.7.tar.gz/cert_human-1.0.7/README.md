[![PyPI version](https://badge.fury.io/py/cert-human.svg)](https://badge.fury.io/py/cert-human)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![Python Versions](https://img.shields.io/pypi/pyversions/cert-human.svg)](https://pypi.org/project/cert-human/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Known Vulnerabilities](https://snyk.io/test/github/lifehackjim/cert_human/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/lifehackjim/cert_human?targetFile=requirements.txt)
[![codecov](https://codecov.io/gh/lifehackjim/cert_human/branch/master/graph/badge.svg)](https://codecov.io/gh/lifehackjim/cert_human)
[![Build Status](https://travis-ci.org/lifehackjim/cert_human.svg?branch=master)](https://travis-ci.org/lifehackjim/cert_human)

Cert Human: SSL Certificates for Humans
=======================================

Description
-----------

Somebody said something about over-engineering. So I obviously had to chime in.

No, but seriously, I was in the midst of rewriting [another project of mine](https://github.com/tanium/pytan), and I wanted to incorporate a method to get an SSL certificate from a server, show the user the same kind of information as you'd see in a browser, prompt them for validity, then write it to disk for use in all [requests](http://docs.python-requests.org/en/master/) to a server.

I was unable to find any great / easy ways that incorporated all of these concepts into one neat thing. So I made a thing.

Originally this was based off of yet another lovely over-engineered solution in [get-ca-py](https://github.com/neozenith/get-ca-py) by [Josh Peak](https://github.com/neozenith).


Installation
------------

To install Cert Human, use pip / pipenv:

``` {.sourceCode .bash}
$ pip install cert_human
```


Documentation
-------------

Available [here](https://cert-human.readthedocs.io/en/latest/)
