Copyright (C) 2017-2019 H. Turgut Uyar <uyar@tekir.org>

Kırlent [#meaning]_ is a collection of utilities for managing educational
content.

:Repository: https://gitlab.com/tekir/kirlent
:Documentation: https://kirlent.readthedocs.io/

The idea is to generate small units of content which can then be composed
into larger units. A unit can contain actual content, or it can also be
a collection that consists of other content units.

Kırlent uses `reStructuredText`_ as its markup language for source files.
It defines some extra syntax to simplify authoring.

The recommended structure all content units as folders under a main folder.
Every document should have the language code as a prefix to its
file extension::

   content
   |- expressions
   |  |- slides.en.rst
   |  `- slides.tr.rst
   `- statements

The output folders for generated items will replicate this hierarchy, as in::

   _build
   |- expressions
   |  |- slides.en.pdf
   |  `- slides.tr.pdf
   `- statement

Kırlent is built on the `doit`_ tool which makes it very easy to support
incremental builds. That is, Kırlent will build an output again only if
any of the relevant input files have changed.

.. [#meaning]

   "Kırlent" is a Turkish word which means a decorative pillow. It originates
   from the Italian word "ghirlanda". It's also the name of `this beauty`_.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _doit: http://pydoit.org/
.. _this beauty: https://htuyar.tumblr.com/image/87196121163
