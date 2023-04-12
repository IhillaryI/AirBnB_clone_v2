#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from os import path
from datetime import datetime
from fabric.api import local, env, run

env.hosts = ["18.207.207.66", "54.90.27.97"]


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if local("mkdir -p versions").failed:
        return None
    if local("tar -cvzf {} web_static".format(file)).failed:
        return None
    return file
