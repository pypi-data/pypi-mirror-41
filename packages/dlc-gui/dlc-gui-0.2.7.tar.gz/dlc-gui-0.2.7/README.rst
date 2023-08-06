dlc-gui
#######

dlc-gui is a GUI written in Qt5 (PySide2) for
`DeepLabCut <https://github.com/AlexEMG/DeepLabCut>`_.

It is a drop-in replacement for the frame labeling GUI.
It seeks to make labeling a pain-free, user-friendly process.

.. image:: https://gitlab.com/d_/dlc-gui/raw/master/screenshot.png
   :width: 75%
   :align: center

.. contents:: **Table of Contents**
    :backlinks: none

Features
========

* Opening of .h5 files
* Saving as a .h5 or .pkl file at any time, and resuming labeling later
* Zoom and scrolling with mousewheel
* WASD keybindings for navigating frames and labels
* Editing of any label of any frame at any time
* Removing labels
* Adjusting dotsize at any time


Installation
============

dlc-gui is distributed on `PyPI <https://pypi.org>`_ as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 3.6+.

.. code-block:: bash

      $ pip install dlc-gui

You can also get the latest development version with:

.. code-block:: bash

      $ pip install git+https://gitlab.com/d_/dlc-gui.git


Usage
=====

Running the GUI
---------------

Inside a Python shell:

   >>> import dlc_gui
   >>> dlc_gui.show()

Inside a command-line shell:

.. code-block:: bash

      $ python -m dlc_gui

It can also be run directly:

.. code-block:: bash

      $ python .../dlc_gui/gui.py

One thing to note is that the GUI looks different (usually worse) when run from inside a virtual environment.

Using the GUI
-------------


Begin by opening a directory full of the frames (\*.png) you want to label, or a .h5/.pkl file from a previous save.

Use left mouse click to add a label at the cursor, or right mouse to remove a label. Switch between frames or bodyparts using the left and right panels, or WASD keybindings.

Save by pressing File>Save, or Ctrl+S. This will save your labeling as a .h5 file that can later be edited.

You can also save as a .pkl file, which is just a `Python pickle <https://docs.python.org/3/library/pickle.html>`_ of the pandas DataFrame object. This is only for just in case saving as a .h5 file fails, so that progress can be saved and resumed after working out any bugs or issues.

Keybindings
~~~~~~~~~~~
+---------------------------------+-------------------------+
|Shortcut                         |Action                   |
+=================================+=========================+
|:kbd:`Left Mouse Button`         |Add label at cursor      |
+---------------------------------+-------------------------+
|:kbd:`Right Mouse Button`        |Remove label             |
+---------------------------------+-------------------------+
|:kbd:`Ctrl` + :kbd:`Mouse Wheel` |Zoom                     |
+---------------------------------+-------------------------+
|:kbd:`Shift` + :kbd:`Mouse Wheel`|Horizontal Scroll        |
+---------------------------------+-------------------------+
|:kbd:`Mouse Wheel`               |Vertical Scroll          |
+---------------------------------+-------------------------+
|:kbd:`W`                         |Previous Frame           |
+---------------------------------+-------------------------+
|:kbd:`A`                         |Previous Bodypart        |
+---------------------------------+-------------------------+
|:kbd:`S`                         |Next Frame               |
+---------------------------------+-------------------------+
|:kbd:`D`                         |Next Bodypart            |
+---------------------------------+-------------------------+
|:kbd:`Ctrl` + :kbd:`F`           |Open a .h5 or .pkl file  |
+---------------------------------+-------------------------+
|:kbd:`Ctrl` + :kbd:`O`           |Open a directory of      |
|                                 |frames                   |
+---------------------------------+-------------------------+
|:kbd:`Ctrl` + :kbd:`S`           |Save as a .h5 file       |
+---------------------------------+-------------------------+


License
=======

dlc-gui is distributed under the terms of the
`LGPL v3 <https://choosealicense.com/licenses/lgpl-3.0>`_.
