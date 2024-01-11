#!/usr/bin/python3
"""makes a .tgz archive"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Creates a .tgz archive."""
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    path = "versions/web_static_{}.tgz".format(time)
    local("mkdir -p versions")

    if local("tar -cvzf {} web_static".format(path)).succeeded:
        return path
    return None

