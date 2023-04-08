#!/usr/bin/python3
"""This Modules contains a function that uses
Fabric to create a directory and generates a .tgz file
"""

from fabric.api import local
from datetime import datetime


def do_pack():
"""Create a tar gzipped archive of the directory web_static."""

    today = datetime.today()
    result = local("mkdir -p versions")
    if result.failed:
        return None

    file_string = f"web_static{today.year}{today.month}{today.day}" \
        f"{today.hour}{today.minute}{today.second}"

    print(f"Packing web_static to version/{file_string}.tgz")
    result = local(f"tar -cvzf versions/{file_string}.tgz web_static")
    if result.failed:
        return None
    return "version/{file_string}"
