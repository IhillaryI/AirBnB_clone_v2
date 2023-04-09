#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["18.207.207.66", "54.90.27.97"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False
    file_string = archive_path.split("/")[1]
    file_name = file_string.split(".")[0]

    if put(archive_path, "/tmp", use_sudo=True).failed:
        return False
    result = run(f"sudo tar xf /tmp/{file_string} -C"
                 f" /data/web_static/releases/ --one-top-level")
    if result.failed:
        return False
    if run(f"sudo rm /tmp/{file_string}").failed:
        return False
    if run(f"sudo rm -rf /data/web_static/current").failed:
        return False
    result = run(f"sudo ln -s /data/web_static/releases"
                 f"/{file_name} /data/web_static/current")
    if result.failed:
        return False
    return True
