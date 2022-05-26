#!/usr/bin/python3
""" Generates a .tgz archive """
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo"""
    from os import mkdir, path

    now = datetime.now()
    filename = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    filepath = "versions/{}".format(filename)

    try:
        mkdir('./versions')
    except FileExistsError:
        pass

    create_file = local("tar -cvzf {} web_static".format(filepath))
    if create_file.failed:
        return None
    return filepath
