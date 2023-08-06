Markup
======

Kırlent markup is based on Sphinx markup. All Sphinx syntax should be valid
Kırlent syntax. You can find the differences for different output types below.


Slides Markup
-------------

Each slide starts with a ``slide`` directive::

   .. slide:: Slide Title

      - point 1
      - point 2

Slides can contain fragments that will be displayed incrementally::

   .. slide:: Slide Title

      - point 1

      .. container :: fragment

         - point 2

For two-column slides, the following template can be used::

   .. slide:: Slide Title

      .. container:: columns

         .. container:: column

            - point 1

         .. container:: column

            - point 2

Slides can have speaker notes::

   .. slide:: Slide Title

      - point 1
      - point 2

      .. speaker-notes::

         speaker notes


Collection Markup
-----------------

If a unit a collection of other units, it has to contain a :file:`parts.txt`
file that lists the names of the source units, one on every line::

   unit1
   unit2
   unit3

.. warning:: This syntax might change very soon.

When generating output the source units will be combined. For example,
if you're building a slide output for a collection, Kırlent will look for
:file:`slides.rst` file under each unit, concatenate them in the given order
and then do a transformation for the result.
