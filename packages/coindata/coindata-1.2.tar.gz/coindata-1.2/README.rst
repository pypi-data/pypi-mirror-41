Coindata
========
|PyPI|
|Python|
|Build Status|
|License|

Daily historical data of all time to date of hundreds of cryptocurrencies.

Use it for machine learning, vector prediction or for whatever you like. Be my guest.

Install
-------

Install with pip or clone, both works.

.. code:: bash

    $ pip install coindata
    ---- or ----
    $ git clone git@github.com:anaxilaus/coindata
    $ python coindata/setup.py install
    
Setup installs requirements itself. Requirements are beautifulsoup4 and requests. 

Usage with Modules
------------------

There are only 2 modules you will use:

::

    snapshot
    parser

Update cache with ``snapshot``
------------------------------

.. code:: python

    >>> coindata.snapshot.take()

Get data with ``parser``
------------------------

.. code:: python

    >>> coindata.parser.vector_of('btc')
        [
          [Beginning of the time]
          . 
          .
          .
          ['Date': string,
           'Open*': float,
           'High': float,
           'Low': float,
           'Close**': float,
           'Volume': float,
           'Market Cap': float,
           # additional info below #
           'date': datetime.object,
           'circulation': decimal,
           'change': float]
           . 
           .
           .
          [Today]
        ]
        

How this works?
---------------
Basically, this program parses daily historical data of all time from coinmarketcap's website, stores at CSV files through running a "snapshot." After you request a data vector, calculates what coinmarketcap doesn't give you, like circulation supply, daily percentage change, datetime object etc. and returns the vector.

If you want, you can use .csv files seperately.

File structure:
---------------

::

    source-code:
        coindata:
            snapshots:
                latest-snapshot:
                    CSV files
            tickers:
                JSON files


`Get documentation for more with built-in help() or read the code.`

Important Notes
---------------

``+ Symbol, name and case doesn't matter.``

::

    btc = BTC = bitcoin = BITCOIN

``+ Based on USD.``

``+ Date notation is ISO8601 in CSV files.``
.. code:: python

    >>> coindata.ISO8601
    "%Y-%m-%d"


Give this a star this if you feel this helped you.

Also, if you want to buy a beer:

::

    BTC: 16XwDdxUaphSX4yWDTTiSfNy2dTyEZ5MLy
    ETH: 0x35F4B63f7eBBB2E6080F7f9f797A068004faf323
    LTC: LdukNLZqzeEvvFYMw98L9Rj8AYvP86BhEe


.. |PyPI| image:: https://badge.fury.io/py/coindata.svg
    :target: https://badge.fury.io/py/coindata
.. |Build Status| image:: https://travis-ci.org/Anaxilaus/coindata.svg?branch=master
    :target: https://travis-ci.org/Anaxilaus/coindata
.. |License| image:: https://img.shields.io/badge/license-MIT-green.svg
    :target: https://github.com/Anaxilaus/coindata/blob/master/LICENSE
.. |Python| image:: https://img.shields.io/badge/Python-3.5|3.6|3.7-blue.svg
    :target: https://github.com/Anaxilaus/coindata/blob/master/.travis.yml
