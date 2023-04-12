#!/usr/bin/python3

from os import path
from datetime import datetime
from fabric.api import local, run, env

env.hosts = ["54.90.27.97", "18.207.207.66"]


def do_pack():
    """Create a tar archive of the directory web_static."""
    dt = datetime.utcnow()
    file = f"versions/web_static_{dt.year}{dt.month}" \
            f"{dt.day}{dt.hour}{dt.minute}{dt.second}.tgz"

    if local("mkdir -p versions").failed:
        return None
    if local(f"tar -czf {file} web_static").failed:
        return None
    return file
