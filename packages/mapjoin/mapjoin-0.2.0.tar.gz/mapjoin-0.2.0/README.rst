mapjoin: the OBSCENE string generation one-liner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The purpose of the mapjoin function is to have an alternative to str.join that
looks more like os.path.join (which takes ``*args``).

``mapjoin()``
=============

.. code-block:: python

   from mapjoin import mapjoin, strjoin

   mapjoin('foo', 2)                      # raise TypeError
   mapjoin('foo', 2, sep='_', key=str)    # return 'foo_2'

   # you can also make mapjoin use your own callback with the key kwarg:
   your_formatter = lambda key: str(key) if key else 'Nothin!'
   mapjoin('foo', obj, 2, None, sep='\n', key=your_formatter)

``strjoin()``
=============

.. code-block:: python

   strjoin('foo', 2)                      # 'foo-2'
   strjoin('foo', 2, sep='_')             # 'foo_2'


But ... why ?
=============

Initially, because I make to many mistakes when I write an os.path.join call and then a
str.join call in a row:

.. code-block:: python

   >>> os.path.join('a', 'b')
   'a/b'

   # and 2 seconds later i'm doing this:

   >>> ' '.join('a', 'b')
   TypeError: join() takes exactly one argument (2 given)

   # and instead of "just fixit and move on", i decided try to make a joint

But also because I can't get no satisfaction with my code when it looks like:

.. code-block:: python

   readable = ' '.join(map(str, [
       'hello',
       f'__{name}__',
       something,
   ]))

   # or:

   def foo():
       readable = textwrap.dedent(f'''
       hello
       __{name}__
       ''').strip()

`Participate to the story
<https://mail.python.org/pipermail/python-ideas/2019-January/054995.html>`_
