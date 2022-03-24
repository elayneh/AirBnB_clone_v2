#!/usr/bin/python3
# full deployment
from fabric.api import *
from os.path import exists
from datetime import datetime


env.hosts = ['34.139.204.59', '3.235.148.75']


def do_pack():
    def do_pack():
        """ method to executed by the fabric """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """the method to be executed in fab"""
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


def deploy():
    """create and distribute the archive to the server"""
    arch_path = do_pack()
    if exists(arch_path) is False:
        return False
    res = do_deploy(arch_path)
    return res
