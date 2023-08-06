PyBEL-OLS |build| |coverage| |documentation|
============================================
A PyBEL [1]_ extension for building BEL resources with the EBI [2]_ Ontology
Lookup Service.

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
Get the Latest
~~~~~~~~~~~~~~~
Download the most recent code from `GitHub <https://github.com/pybel/pybel-ols>`_ with:

.. code-block:: sh

   $ pip install git+https://github.com/pybel/pybel-ols.git

For Developers
~~~~~~~~~~~~~~
Clone the repository from `GitHub <https://github.com/pybel/pybel-ols>`_ and install in editable mode with:

.. code-block:: sh

   $ git clone https://github.com/pybel/pybel-ols.git
   $ cd pybel-ols
   $ pip install -e .

Getting Started
---------------
The main goal is to generate a namespace file. For example, to generate a namespace for the `Human Phenotype Ontology
<https://www.ebi.ac.uk/ols/ontologies/hp>`_, abbreviated with the prefix ``hp``, the following command can be used:

.. code-block:: sh

   $ pybel-ols namespace_from_ols hp --encoding "O" --output ~/Desktop/hp.belns

Where ``--encoding "O"`` tells it that all terms in this ontology correspond to the pathology/phenotype BEL type.

Alternatively, the '-b' option can be used to specify an alternate OLS instance

.. code-block:: bash

    $ pybel-ols namespace_from_ols hp --encoding O --output ~/Desktop/hp.belns -b https://localhost/ols

References
----------
.. [1] Hoyt, C. T., *et al.* (2017). `PyBEL: a Computational Framework for Biological Expression Language
       <https://doi.org/10.1093/bioinformatics/btx660>`_. Bioinformatics, 34(December), 1–2.

.. [2] Cote, R., *et al.* (2006). `The Ontology Lookup Service, a lightweight cross-platform tool for controlled
       vocabulary queries <https://doi.org/10.1186/1471-2105-7-97>`_. BMC Bioinformatics, 7, 1–7.

.. |build| image:: https://travis-ci.org/pybel/pybel-ols.svg?branch=master
    :target: https://travis-ci.org/pybel/pybel-ols
    :alt: Build Status

.. |coverage| image:: https://codecov.io/gh/pybel/pybel-ols/coverage.svg?branch=master
    :target: https://codecov.io/gh/pybel/pybel-ols?branch=master
    :alt: Coverage Status

.. |documentation| image:: https://readthedocs.org/projects/pybel-ols/badge/?version=latest
    :target: https://pybel.readthedocs.io/projects/ols/en/latest/?badge=latest
    :alt: Documentation Status

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/pybel-ols.svg
    :alt: Stable Supported Python Versions

.. |pypi_version| image:: https://img.shields.io/pypi/v/pybel-ols.svg
    :alt: Current version on PyPI

.. |pypi_license| image:: https://img.shields.io/pypi/l/pybel-ols.svg
    :alt: MIT License
