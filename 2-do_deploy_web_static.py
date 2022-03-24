#!/usr/bin/python3
""" deploy some contents"""


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['34.139.204.59', '3.235.148.75']


def do_deploy(archive_path):
    """ method to executed
    """
    if exists(archive_path) is False:
        return False
    file = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(file.split('.')[0])
    temp = "/tmp/" + file

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(temp, no_tgz))
        run("rm {}".format(temp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True
    except:
        return False
