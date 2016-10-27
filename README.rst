
.. image:: https://d18m5nnl28b2pp.cloudfront.net/p/a/img/header.png

.. image:: https://scrutinizer-ci.com/g/sandcage/sandcage-api-python/badges/quality-score.png?b=master
    :target: https://scrutinizer-ci.com/g/sandcage/sandcage-api-python/?branch=master
.. image:: https://travis-ci.org/sandcage/sandcage-api-python.svg?branch=master
    :target: https://travis-ci.org/sandcage/sandcage-api-python

sandcage-api-python is a python library for interfacing with SandCage's API. The API documentation can be found at `SandCage's API documentation <https://www.sandcage.com/docs/0.2/>`_


Requirements
------------
- certifi
- requests

In order to use the library you need an API KEY from `SandCage <https://www.sandcage.com>`_.

Install
-------
``python setup.py install``

Usage
-----

Simply::
  
  from sandcage import SandCage

  sc = SandCage('[YOUR_SANDCAGE_API_KEY]')
  sc.list_files_service()

See more `examples <examples/>`_

To not include YOUR_SANDCAGE_API_KEY into your code you can for example save it as a file named SANDCAGE_API_KEY into your home directory::

  cd ~
  echo YOUR_SANDCAGE_API_KEY > SANDCAGE_API_KEY

and then use the following code to initialize SandCage::

  import os.path
  from sandcage import SandCage

  api_key_dir = os.path.expanduser('~')
  api_key_file = os.path.join(api_key_dir, 'SANDCAGE_API_KEY')
  with open(api_key_file, 'r') as f:
      api_key = f.readline()

  sc = SandCage(api_key=api_key)
