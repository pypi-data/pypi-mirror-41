Dredging
========
Collection of helper functions for dredging math written in python

Installation and use
====================
Instal from pypi
----------------
.. code:: bash

  pip install dredging

Calculate productivity
----------------------
  >>> from dredging import productivity
  >>> productivity(crosssectional_area=.496, mean_density=1111.27,
                   mean_speed=1.34, material_density=1760,
                   material_porosity=.3, water_density=1014,
                   coeff1=0.9, coeff2=1.1, timedelta=2.5),

Default values
--------------
.. code:: python

  coeff1 = 0.9
  coeff2 = 1.1
  water_density = 1000
  timedelta = 1

Notes
-----
All values in SI
