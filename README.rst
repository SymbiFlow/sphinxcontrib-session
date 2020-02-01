.. highlight:: rst

Sphinx Contrib Session
======================

.. contents:: Table of contents

Setting Up
----------

In ``conf.py`` add ``'sphinxcontrib_session'`` to the list of extensions as
shown below (note the underscore);

.. code-block:: python
        :caption: conf.py
        :emphasize-lines: 8

        # Add any Sphinx extension module names here, as strings. They can be
        # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
        # ones.
        extensions = [
            'sphinx.ext.intersphinx',
            'sphinx.ext.todo',
            'sphinx.ext.githubpages',
            'sphinxcontrib_session',
        ]


Syntax
------

The ``.. session::`` directive should be a drop in replacement for the
``..  code-block::`` directive and support the same set of options.

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block

.. code:: rst

    .. session:: [<language> [<prompts> [<modifier>]]]

       <statements>

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive:option-code-block-linenos
``:linenos:`` is supported but generally doesn't make much sense.
https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive:option-code-block-lineno-start


.. rst:directive:: .. session:: [language]

   Example::

      .. session:: ruby

         Some Ruby code.

   This directive takes a language name as an argument.

   .. rubric:: options

   .. rst:directive:option:: linenos
      :type: no value

      Enable to generate line numbers for the code block::

         .. session:: ruby
            :linenos:

            Some more Ruby code.

   .. rst:directive:option:: lineno-start: number
      :type: number

      Set the first line number of the code block.  If present, ``linenos``
      option is also automatically activated::

         .. session:: ruby
            :lineno-start: 10

            Some more Ruby code, with line numbering starting at 10.

   .. rst:directive:option:: emphasize-lines: line numbers
      :type: comma separated numbers

      Emphasize particular lines of the code block::

       .. session:: python
          :emphasize-lines: 3,5

          def some_function():
              interesting = False
              print 'This line is highlighted.'
              print 'This one is not...'
              print '...but this one is.'


   .. rst:directive:option: force
      :type: no value

      Ignore minor errors on highlighting

   .. rst:directive:option:: caption: caption of code block
      :type: text

      Set a caption to the code block.

   .. rst:directive:option:: name: a label for hyperlink
      :type: text

      Define implicit target name that can be referenced by using
      :rst:role:`ref`.  For example::

        .. session:: python
           :caption: this.py
           :name: this-py

           >>> print 'Explicit is better than implicit.'
           Explicit is better than implicit.

   .. rst:directive:option:: dedent: number
      :type: number

      Strip indentation characters from the code block. For example::

         .. session:: ruby
            :dedent: 4

                some ruby code

   .. rst:directive:option:: force
      :type: no value

      If given, minor errors on highlighting are ignored.


Supported Session Types
~~~~~~~~~~~~~~~~~~~~~~~

In theory any 'session' lexer
`supported by Pygments <https://pygments.org/docs/lexers/>`__ should work.

The tested sessions are:

- ``BashSessionLexer`` https://pygments.org/docs/lexers/#pygments.lexers.shell.BashSessionLexer - also known as `console` and `shell-session`.

- ``MSDOSSessionLexer`` https://pygments.org/docs/lexers/#pygments.lexers.shell.MSDOSSessionLexer - also known as `doscon`.

- ``PowerShellSessionLexer`` https://pygments.org/docs/lexers/#pygments.lexers.shell.PowerShellSessionLexer - also known as `ps1con`.

- ``TcshSessionLexer`` https://pygments.org/docs/lexers/#pygments.lexers.shell.TcshSessionLexer - also known as `tcshcon`


- https://pygments.org/docs/lexers/#pygments.lexers.python.PythonConsoleLexer
- https://pygments.org/docs/lexers/#pygments.lexers.r.RConsoleLexer

- https://pygments.org/docs/lexers/#pygments.lexers.sql.PostgresConsoleLexer
- https://pygments.org/docs/lexers/#pygments.lexers.sql.SqliteConsoleLexer
- https://pygments.org/docs/lexers/#pygments.lexers.ruby.RubyConsoleLexer

Lexers are wanted for;

- GDB debugging session.
- TCL script session.


Examples
--------

See: https://sphinxcontrib-session.rtfd.io/

