#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import local, cd, run, put, env

env.hosts = ["18.207.207.66", "54.90.27.97"]
env.user = "ubuntu"


def do_deploy(archive_path):
    if not os.path.isfile(archive_path):
        return False
    file_name = os.path.relpath(archive_path).split("/")[1]

    if put(archive_path, "/tmp", use_sudo=True).failed:
        return False
    result = run(f"sudo tar xf /tmp/{file_name} -C"
                 f" /data/web_static/releases/ --one-top-level")
    if result.failed:
        return False
    if run(f"sudo rm /tmp/{file_name}").failed:
        return False
    if run("sudo rm -rf /data/web_static/current").failed:
        return False
    result = run(f"sudo ln -s /data/web_static/releases"
                 f"/{file_name.split('.')[0]} /data/web_static/current")
    if result.failed:
        return False
    return True
