#!/usr/bin/python3

from os import path
from fabric.api import local, run, env, put, cd

env.hosts = ["54.90.27.97", "18.207.207.66"]


def do_deploy(archive_path):
    """Deploys the archive to the server and Sets up the web_static files to be
    displayed in the right location
    Args:
        archive_path (str): the path to the archive file
    Returns:
        True (bool): If all runs successfully
        False (bool): If it runs poorly
    """
    if not path.isfile(archive_path):
        return False

    archive = archive_path.split("/")[1]
    file = archive.split(".")[0]

    if put(archive_path, "/tmp").failed:
        return False
    if run("sudo mkdir -p /data/web_static/releases/{}".format(file)).failed:
        return False
    if run("sudo tar -xf /tmp/{}".format(archive)).failed:
        return False
    if cd("/tmp").failed:
        return False
    if run("sudo cp -r web_static/*"
            " /data/web_static/releases/{}".format(file)).failed:
        return False
    if run("sudo rm -rf web_static*".format(archive)).failed:
        return False
    if cd("/data/web_static/").failed:
        return False
    if run("sudo rm -rf current").failed:
        return False
    if run("sudo ln -s releases/{} current".format(file)).failed:
        return False
    return True
