dlc-gui
=======

dlc-gui is a GUI written in Qt5 (PySide2) for `DeepLabCut <https://github.com/AlexEMG/DeepLabCut>`_.

It is a drop-in replacement for ``labeling_toolbox.py`` (``>>> deeplabcut.label_frames(config)``)

|pypi|

.. contents:: **Table of Contents**
    :backlinks: none

Installation
------------

dlc-gui is distributed on `PyPI <https://pypi.org>`_ as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 3.5+.

.. code-block:: bash

      $ pip install dlc-gui

Usage
_____

Inside a Python shell:

.. code-block:: python

      >>> import dlc_gui
      >>> dlc_gui.show()

Inside a command-line shell:

.. code-block:: bash

     $ python -m dlc_gui

License
-------

dlc-gui is distributed under the terms of the
`LGPL v3 <https://choosealicense.com/licenses/lgpl-3.0>`_.

.. |pypi| image:: https://img.shields.io/pypi/v/dlc-gui.svg?style=flat-square
      :target: https://pypi.org/project/dlc-gui
