LeapPythonTest
==============

start LeapMotion with Python


How to start

``
python Sample.py
``
 
If it couldn't work, please check a path.

``
otool -L LeapPython.so
``

then change them Path

``
  install_name_tool -change "current path" "new path" LeapPython.so
``
