#!/usr/bin/python3
# clean out of dated archive from the deployment
from fabric.api import *
import os

env.hosts = ['34.139.204.59', '3.235.148.75']


def do_clean(number=0):
    """remove out-dated archives
    """

    number = 1 if int(number) == 0 else int(number)

    archs = sorted(os.listdir("versions"))
    [archs.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archs]

    with cd("/data/web_static/releases"):
        archs = run("ls -tr").split()
        archs = [a for a in archs if "web_static_" in a]
        [archs.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archs]
