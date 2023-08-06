*rnaviewparser* is a simple parser for `RNAVIEW`_ filename.pdb.out files.

.. _RNAVIEW: http://ndbserver.rutgers.edu/ndbmodule/services/download/rnaview.html
.. _ply: https://www.dabeaz.com/ply/"

It uses `ply`_ for the lexing/parsing bit and python dataclasses to store the data.
It allows an export to CSV files.

It works with Python 3.7.

:Author: Maria Climent-Pommeret (Chopopope)
:License: MIT License
:Homepage: https://gitlab.climent-pommeret.red/Chopopope/rnaviewparser

Installating
------------

Please install in a virtual environment that uses Python3.7 by typing::

    pip install rnaviewparser

Usage example
-------------
Consider this::

    In[1]: from rnaviewparser import rnaviewparser

    In[2]: basepairs = rnaviewparser.RnaviewParser("~/playground/tr0001.pdb.out").parse()

    In[3]: factory = basepairs.generate_interactions()

    In[4]: wh = factory["W/H"]

    In[5]: wh.pretty()
    Out[5]:
    +------------------+-------------+-------+
    | Interaction type | Orientation | Total |
    +------------------+-------------+-------+
    |       std        |     cis     |   0   |
    |       std        |    trans    |   0   |
    +------------------+-------------+-------+
    
    In[6]: basepairs.csv("/tmp/foo.csv")

    In[7]: ww = factory["W/W"]

    In[8]: ww.find_interaction_by_position(8)
    Out[8]:
    (1,
     [BasePair(orientation='cis', position_1=1, position_2=72, base_1='G', base_2='C', interaction_type='+/+')])
```
