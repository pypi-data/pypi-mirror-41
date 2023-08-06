This is for reading and writing stock data

Data storage
~~~~~~~~~~~~

::

   -path
   --files
       filename_20180102.csv
       filename_20180103.csv
       .
       .
       .
       filename_20181231.csv

This new version package (still under construction) would also support
data stored like below

::

   -path
   --files
       filename_A.csv
       filename_B.csv
       .
       .
       .

Read csv with different structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  example1

.. code:: python

   ticker1,value1
   ticker2,value2
   ticker3,value3
   ticker4,value4

to read this type of csv file, use

.. code:: python

   read_df(path='path',file_pattern='filename')

-  example2

.. code:: python

   stkid,open,high,low,close
   ticker1,o1,h1,l1,c1
   ticker2,o2,h2,l2,c2
   ticker3,o3,h3,l3,c3

to read ``open``, use

.. code:: python

   Open=read_df(path='path',file_pattern='filename',dat_col='open')

to read ``open`` and ``close``, use

.. code:: python

   Open,Close=read_df(path='path',file_pattern='filename',dat_col=['open','close'])

to return a multi index dataframe, use

.. code:: python

   Price=read_mdf(path='path',file_pattern='filename',dat_col=['open','close'])

Write
~~~~~

-  dataframe example

.. code:: python

               ticker1     ticker2     ticker3
   20180101     10.32       20.22        12.35
   20180102      NaN        20.10        13.31
   20180105      NaN        20.10        12.12

use ``write_df`` to write data of each date to one csv file

-  dictionary example

each value in the dictionary should be a dataframe and be like the
example showed above

.. code:: python

   write_factors(path='path',file_pattern='filename',**dictionary)

Notice
~~~~~~

Default reading trading calendar is Chinese market trading calendar, to
change the calendar use ``dt_range`` option to input all dates.


