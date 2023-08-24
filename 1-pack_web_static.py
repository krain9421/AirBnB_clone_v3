#!/usr/bin/python3
"""Generates a .tgz archive from the contents of web_static"""
import os
from datetime import datetime
from fabric.api import *


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    date = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date.year,
        date.month,
        date.day,
        date.hour,
        date.minute,
        date.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        output = None
    return output
