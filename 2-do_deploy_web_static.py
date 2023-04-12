#!/usr/bin/python3

from os import path
from fabric.api import local, run, env

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
    pass
