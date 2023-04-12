#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy"""
import os.path
from datetime import datetime
from fabric.api import local, env, run
