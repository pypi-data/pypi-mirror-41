===============================
csv2athena_schema
===============================

.. image:: https://badge.fury.io/py/csv2athena_schema.png
    :target: http://badge.fury.io/py/csv2athena_schema

.. image:: https://travis-ci.org/yuokada/csv2athena_schema.png?branch=master
        :target: https://travis-ci.org/yuokada/csv2athena_schema

.. image:: https://pypip.in/d/csv2athena_schema/badge.png
        :target: https://crate.io/packages/csv2athena_schema?version=latest


A Python Script to build a athena create table from csv file

Features
--------

* TODO

Install & Setup
---------------

.. code-block:: bash

    $ git clone https://github.com/yuokada/csv2athena_schema.git
    $ pip3 install -r requirements.txt



Execute script
--------------

.. code-block:: bash

    $ python3 scripts/csv2athena_schema.py \
    --table-properties skip.header.line.count=1 has_encrypted_data=false \
    --schema your_schema \
    --location 's3://your_bucket/path_to_csv'
    /path/to/your.csv


Requirements
------------

- Python >= 3.5

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/yuokada/csv2athena_schema/blob/master/LICENSE>`_ file for more details.


Link
----

- `sloria/cookiecutter-docopt: A Python command-line script template that uses docopt for arguments parsing <https://github.com/sloria/cookiecutter-docopt>`_
- `okfn/messytables: Tools for parsing messy tabular data. This is now superseded by https://github.com/frictionlessdata/tabulator-py <https://github.com/okfn/messytables>`_
- `pallets/jinja: The Jinja2 template engine <https://github.com/pallets/jinja>`_
- `Flake8: Your Tool For Style Guide Enforcement — flake8 3.7.2 documentation <http://flake8.pycqa.org/en/latest/>`_

Athena

- `CREATE TABLE - Amazon Athena <https://docs.aws.amazon.com/athena/latest/ug/create-table.html>`_
- `SerDe Reference - Amazon Athena <https://docs.aws.amazon.com/athena/latest/ug/serde-reference.html>`_
- `Compression Formats - Amazon Athena <https://docs.aws.amazon.com/athena/latest/ug/compression-formats.html>`_