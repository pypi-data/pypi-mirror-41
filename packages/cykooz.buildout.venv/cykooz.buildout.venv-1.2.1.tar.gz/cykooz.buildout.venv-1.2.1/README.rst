**cykooz.buildout.venv** is a `zc.buildout`_ extension that creates virtual
python environment and use it to run buildout.

.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout

Usage
*****

Add ``cykooz.buildout.venv`` to the ``extensions`` entry in your ``[buildout]``
section::

    [buildout]
    extensions = cykooz.buildout.venv

This enables additional ``[buildout]`` option:

``venv-directory``
  This specifies the directory where virtual environment will be
  created. Defaults to ``parts/venv``.

  If this directory already has a virtual python environment and it
  version is equal to version of python used to run buildout,
  then this environment will be used to run buildout without any changes.

Full example
============
::

    [buildout]
    extensions = cykooz.buildout.venv
    venv-directory = ${buildout:parts-directory}/myvenv
