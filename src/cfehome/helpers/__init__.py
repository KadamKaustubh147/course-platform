from ._cloudinary import cloudinary_init

__all__ = ["cloudinary_init"]

'''
what is __init__.py

__init__.py is a special file in Python that is used to initialize a directory as a Python package. When a directory contains an __init__.py file, Python treats that directory as a package, allowing you to import other modules and sub-packages within it.

Key Purposes of __init__.py
Package Initialization:

It helps Python recognize the directory as a package. Without an __init__.py file, Python would not treat the directory as a package, and you wouldn’t be able to import modules or files within it as part of that package.
Control Imports:

By adding imports within __init__.py, you can control what gets imported when someone imports the package directly.
You can use __all__ in __init__.py to specify which modules, classes, or functions should be exposed as part of the package.
Package-Level Variables or Configuration:

'''




"""
In Python, __all__ is a special variable used in a module (often within the __init__.py file) to define a list of public symbols (functions, classes, variables) that the module explicitly exports when using from module import *.

Purpose of __all__
Explicit Export: It provides a list of symbols that should be publicly accessible when a wildcard import (from module import *) is used.
Encapsulation: It hides other module-level variables, functions, or classes that aren’t listed in __all__, essentially acting as a filter for the API of the module.
Clarity: It helps maintainers and users understand which functions or classes are intended for public use.
"""