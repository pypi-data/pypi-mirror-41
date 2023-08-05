Python Backscatter
==================
.. image:: https://readthedocs.org/projects/backscatter/badge/?version=latest
    :target: https://backscatterio.readthedocs.io/en/latest/?badge=latest

.. image:: https://badge.fury.io/py/backscatter.svg
    :target: https://badge.fury.io/py/backscatter

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT

This is an abstract python library built on top of the `Backscatter`_ service. It is preferred that users use this library when implementing integrations or plan to use Backscatter within their code. The library includes a small client to interact with the API.

.. _Backscatter: https://backscatter.io/

Quick Start
-----------
**Install the library**:

``pip install  backscatter`` or ``python setup.py install``

**Save your configuration**:

``backscatter setup --api-key <your-API-key>``

**Search observations**:

``backscatter observations --query 148.227.224.17``

**Get Trends**:

``backscatter trends --type port``

**Enrich values**:

``backscatter enrich --query 148.227.224.17``

Features
--------
* Run observation searches for ip, network, asn, country and ports
* Get trend data for all data types

Changelog
---------
01-21-19
~~~~~~~~
* Feature: Added enrichment support
* Feature: Added JSON and table output formats
* Change: Adjusted query type to be optional if value is mapped to a type

01-13-19
~~~~~~~~
* Bugfix: Resolved undeclared var in client observations call

01-12-19
~~~~~~~~
* Initial launch of the library