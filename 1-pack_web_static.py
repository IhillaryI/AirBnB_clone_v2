#!/usr/bin/python3
"""This Modules contains a function that uses
Fabric to create a directory and generates a .tgz file
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Packing web_static to a .tgz file.
    Also creates the versions directory if
    it doesn't exist

    All files in the folder web_static must be added to the final archive.
    All archives must be stored in the folder versions.
    """

    today = datetime.today()
    local("mkdir -p versions")

    file_string = f"web_static{today.year}{today.month}{today.day}" \
        f"{today.hour}{today.minute}{today.second}"

    print(f"Packing web_static to version/{file_string}.tgz")
    result = local(f"tar -cvzf versions/{file_string}.tgz web_static")
    if result.failed:
        return None
    return "version/{file_string}"
