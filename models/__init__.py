#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os


HBNB_TYPE_STORAGE = os.environ.get('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'fs':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

else:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()