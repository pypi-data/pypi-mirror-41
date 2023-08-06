Installation
============

You can install Kırlent via PyPI::

   $ pip install kirlent

Kırlent depends on external programs to generate the output items.
According to the type of output you want to generate, you have to install
the necessary tools.

At the moment, only HTML slides and PDF slides can be generated.

To generate HTML slides you need to install ``kirlent_sphinx``.

Kırlent uses `Decktape`_ to convert these HTML slides into PDF. It expects
the command :command:`decktape` to be in the path. Decktape can be installed
using npm::

  $ npm install -g decktape

.. _Decktape: https://github.com/astefanutti/decktape
