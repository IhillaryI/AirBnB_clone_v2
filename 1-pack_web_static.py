#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """Packing web_static to a .tgz file"""

    today = datetime.today()
    local("mkdir -p versions")

    file_string = f"web_static{today.year}{today.month}{today.day}" \
        f"{today.hour}{today.minute}{today.second}"

    print(f"Packing web_static to version/{file_string}.tgz")
    result = local(f"tar -cvzf versions/{file_string}.tgz web_static")
    if result.failed:
        return None
    return "version/{file_string}"
