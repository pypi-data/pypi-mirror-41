Changelog
#########

All notable changes to this project will be documented in this file.

The format is based on `Keep a
Changelog <https://keepachangelog.com/en/1.0.0/>`__, and this project
adheres to `Semantic
Versioning <https://semver.org/spec/v2.0.0.html>`__.

0.2.7_
===========

Added
-----
- Unit testing, even for the GUI

Changed
-------
- Switched from pyyaml to ruamel.yaml
- Switched from native to non-native Qt file dialogs
- A lot of restructured code

Fixed
-----
- A lot of bugs, especially the bug where the scene wasn't being cleared so memory usage was steadily increase

0.2.2_ - 2019-01-27
===================

Added
-----
- Saving and loading a pickle file, just in case saving as a h5 file doesn't work

Fixed
-----
- Bug that prevented saving as a h5 file after a directory of frames was opened
- Bug that truncated the list of frames when opening a h5 file

0.2.0_ - 2019-01-27
===================

Added
-----
- Sphinx docs

Changed
-------
- Help dialog replaced with hyperlink to online docs
- Labels now have color icons rather than color backgrounds

0.1.1_ - 2019-01-26
===================

Added
-----
- More descriptive README with features list and screenshot
- this changelog

Fixed
-----
- Fix bug of loading images from the current directory

0.1.0_ - 2019-01-25
===================

Added
-----
- Slider for selecting label dot size
- WASD bindings for navigating frames and bodyparts

0.0.3_ - 2019-01-25
===================
Added
-----
- Main GUI from qt branch of UnicodeAlt255's fork of DeepLabCut

0.0.1 - 2019-01-25
==================

Added
-----
- Hatch init

.. _Unreleased: https://gitlab.com/d_/dlc-gui/compare/v0.2.7...master
.. _0.2.6: https://gitlab.com/d_/dlc-gui/compare/v0.2.2...v0.2.7
.. _0.2.2: https://gitlab.com/d_/dlc-gui/compare/v0.2.0...v0.2.2
.. _0.2.0: https://gitlab.com/d_/dlc-gui/compare/v0.1.1...v0.2.0
.. _0.1.1: https://gitlab.com/d_/dlc-gui/compare/v0.1.0...v0.1.1
