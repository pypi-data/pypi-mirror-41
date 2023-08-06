Usage
=====

Kırlent has commands for generating various types of output:

- For HTML presentations, it uses RevealJS and the command is ``rv``.
- For PDF presentations, it uses Decktape and the command is ``dt``.

These commands take the unit to generate as their parameter. So, to generate
an HTML presentation from slide sources, run the command::

   $ kirlent rv expressions

And for a PDF presentation::

   $ kirlent dt expressions

To clean up, use the ``clean`` command::

   $ kirlent clean expressions
