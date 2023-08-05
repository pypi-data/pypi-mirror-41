dlc-gui
#######

dlc-gui is a GUI written in Qt5 (PySide2) for
`DeepLabCut <https://github.com/AlexEMG/DeepLabCut>`_.

It is a drop-in replacement for the frame labeling GUI.

.. image:: ./screenshot.png
   :width: 75%
   :align: center

.. contents:: **Table of Contents**
    :backlinks: none

Features
========

* Opening of .h5 files
* Save as a .h5 file at any time, and resume labeling later
* Zoom and scrolling with mousewheel
* WASD keybindings for navigating frames and labels
* Remove labels
* Adjust dotsize


Installation
============

dlc-gui is distributed on `PyPI <https://pypi.org>`_ as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 3.5+.

.. code-block:: bash

      $ pip install dlc-gui


Usage
=====

Inside a Python shell:

   >>> import dlc_gui
   >>> dlc_gui.show()

Inside a command-line shell:

.. code-block:: bash

      $ python -m dlc_gui

It can also be run directly:

.. code-block:: bash

      $ python .../dlc_gui/main.py


License
=======

dlc-gui is distributed under the terms of the
`LGPL v3 <https://choosealicense.com/licenses/lgpl-3.0>`_.
