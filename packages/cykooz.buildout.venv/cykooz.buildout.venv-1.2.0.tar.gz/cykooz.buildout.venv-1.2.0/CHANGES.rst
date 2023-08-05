..  Changelog format guide.
    - Before make new release of core egg you MUST add here a header for new version with name "Next release".
    - After all headers and paragraphs you MUST add only ONE empty line.
    - At the end of sentence which describes some changes SHOULD be identifier of task from our task manager.
      This identifier MUST be placed in brackets. If a hot fix has not the task identifier then you
      can use the word "HOTFIX" instead of it.
    - At the end of sentence MUST stand a point.
    - List of changes in the one version MUST be grouped in the next sections:
        - Features
        - Changes
        - Bug Fixes
        - Docs

Changelog
*********

1.2.0 (2019-01-22)
==================

Changes
-------

- Added checking of version of python in exists venv directory and
  recreate venv if the version is not equal to current python version.

1.1.0 (2016-08-13)
==================

Features
--------

- Added support for Windows.

1.0.1 (2016-08-12)
==================

- First release.
