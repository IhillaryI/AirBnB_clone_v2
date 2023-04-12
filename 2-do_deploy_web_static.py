#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from os import path
from datetime import datetime
from fabric.api import local, put, env, run

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


def do_deploy(archive_path):
    """Deploy a tar gzipped archive to remote web servers."""
    if not path.isfile(archive_path):
        return False
    archive = archive_path.split("/")[1]
    file_name = archive.split(".")[0]

    if put(archive_path, "/tmp").failed:
        return False
    if run(f"sudo tar xf /tmp/{archive} -C /data/web_static/releases/"
            f" --one-top-level").failed:
        return False
    if run(f"rm /tmp/{archive}").failed:
        return False
    if run(f"sudo rm -rf /data/web_static/current").failed:
        return False
    if run(f"sudo ln -s /data/web_static/releases/{file_name} "
            f"/data/web_static/current").failed:
        return False
    if run(f"sudo cp -r /data/web_static/releases/{file_name}/web_static/*"
            f" /data/web_static/releases/{file_name}").failed:
        return False
    if run(f"sudo rm -rf "
            f"/data/web_static/releases/{file_name}/web_static").failed:
        return False
    return True
