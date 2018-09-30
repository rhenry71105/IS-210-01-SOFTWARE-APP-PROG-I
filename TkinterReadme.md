#####################################################
Rickardo's Module:Tkinter
#####################################################

**What's Tkinter?**

=========================================================================================================================
The Tkinter module (“Tk interface”) is the standard Python interface to the Tk GUI toolkit from Scriptics
--(formerly developed by Sun Labs)--. Tk offers a native look and feel on all platforms.
Tkinter consists of a number of modules. The Tk interface is provided by a binary extension module named _tkinter.
This module contains the low-level interface to Tk, and should never be used directly by application programmers.
It is usually a shared library (or DLL), but might in some cases be statically linked with the Python interpreter.
The public interface is provided through a number of Python modules.
The most important interface module is the Tkinter module itself.
To use Tkinter, all you need to do is to import the Tkinter module:

* import Tkinter

* Or, more often:

* from Tkinter import *

==============================================================================================================================
The Tkinter module only exports widget classes and associated constants, so you can safely use the from-in form in most cases.
If you prefer not to, but still want to save some typing, you can use import-as:
import Tkinter as Tk
==============================================================================================================================

Python offers multiple options for developing GUI (Graphical User Interface).
Out of all the GUI methods, tkinter is most commonly used method.
It is a standard Python interface to the Tk GUI toolkit shipped with Python.
Python with tkinter outputs the fastest and easiest way to create the GUI applications.
Creating a GUI using tkinter is an easy task.

To create a tkinter:
1. Importing the module – tkinter
2. Create the main window (container)
3. Add any number of widgets to the main window
4. Apply the event Trigger on the widgets.

===============================================================================================================================

I have created a simple interface using tkinter module GUI (Graphical User Interface) with an Input and submit function.
The interface accepts clear type text and confirms what you have entered was received successfully.
The program has a terminate function added in the interface.
