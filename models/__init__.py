#!/usr/bin/python3

"""
__init__.py is used to mark directories on disk as Python package directories
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
