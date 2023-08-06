# django_docker_engine 

[![Build Status](https://travis-ci.org/refinery-platform/django_docker_engine.svg?branch=master)](https://travis-ci.org/refinery-platform/django_docker_engine)
[![PyPI version](https://badge.fury.io/py/django-docker-engine.svg)](https://pypi.org/project/django-docker-engine/)
![Python versions](https://img.shields.io/pypi/pyversions/django_docker_engine.svg)
![Django versions](https://img.shields.io/pypi/djversions/django_docker_engine.svg)
    
This Django app manages and proxies requests to Docker containers.
The primary goal has been to provide a visualization framework for the
[Refinery Project](https://github.com/refinery-platform/refinery-platform),
but nothing should prevent its use in other contexts, as well.

In order for a Docker container to work with this package it must at a minimum:

- listen on some port for HTTP connections, and
- accept a single JSON file as input.

## Quick Demo

Install [Docker](https://store.docker.com/search?offering=community&type=edition)
if you haven't already, then download the project, install dependencies, and
run the demo server:

```
$ git clone https://github.com/refinery-platform/django_docker_engine.git
$ cd django_docker_engine
$ pip install -r requirements-dev.txt
$ pip install -r requirements.txt
$ ./manage.py runserver
```

Visit the [demo server](http://localhost:8000/): From there you can pick a visualization
tool and a data file to launch a container, see the requests made against
each container, and kill the containers you've launched.

## Motivation

Visualization tools have been built with a range of languages and they may have numerous, and possibly conflicting, dependencies. For the [Refinery Platform](http://refinery-platform.org), a data management, analysis, and visualization system for bioinformatics and computational biology applications, we have tried to accommodate the widest range of tools by creating `django_docker_engine`, a Python package, available on PyPI, which launches Docker containers, proxies requests from Django to the containers, and records each request.

For each tool the wrapping Docker container will parse the input data provided on launch and start listening for requests. Currently, wrappers are in use for pure JavaScript applications, and for client-server applications, such as [HiGlass](http://higlass.io) for exploring genomic contact matrices, and a [Plotly Dash tool](https://github.com/refinery-platform/heatmap-scatter-dash) for gene expression data. The containers themselves may run on the same host as Django, or on separate instances. 

In the Refinery Platform, interactive visualizations managed by `django_docker_engine` complement workflows managed by Galaxy: Both tools lower barriers to entry and make it possible for end users to run sophisticated analyses on their own data. Refinery adds user management, access control, and provenance tracking facilities to make research more reproducible.

`django_docker_engine` will be useful in any environment which needs to provide access to pre-existing or independently developed tools from within a Django application with responsibility for user authentication, access control, and data management.


## More information

For the demo server, [`tools.py`](demo_path_routing_auth/tools.py) defines the tools
which are available and specifies default inputs. Analogously,
the [`visualization-tools` repo](https://github.com/refinery-platform/visualization-tools)
defines the tools which can be loaded into Refinery.

More information:
- [for users of the library](README-USERS.md)
- [for developers of the library](README-DEVS.md)
- [for developers of visualizations](README-VIS.md)
- [background reading](notes)
- [API documentation](https://www.pydoc.io/pypi/django-docker-engine-0.0.57/)
- [BOSC 2018 poster](https://f1000research.com/posters/7-1078)

## Release process

In your branch update VERSION.txt, using semantic versioning:
When the PR is merged, the successful Travis build will push a new version to pypi.