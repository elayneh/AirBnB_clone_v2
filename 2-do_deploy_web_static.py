#!/usr/bin/python3
""" deploy"""

from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['34.139.204.59', '3.235.148.75']  

def do_deploy(archive_path):

    if exists(archive_path) is False:
        return False  
    files = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(files.split('.')[0])
    tmp = "/tmp/" + files

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True
    except:
        return False