#!/usr/bin/python3
# clean out of dated archive from the deployment
from fabric.api import *
import os
from datetime import datetime
env.hosts = ['34.139.204.59', '3.235.148.75']


def do_clean(number=0):
    """remove out-datedarchives"""

    number = 1 if int(number) == 0 else int(number)

    archs = sorted(os.listdir("version"))
    [archs.pop() for elt in range(number)]
    with lcd("version"):
        [local("rm ./{}".format(item)) for item in archs]
    with cd("/data/web_static_releases"):
        archs = run("ls -tr").split()
        archs = [item for item in archs if "web_static_" in item]
        [archs.pop() for item in range(number)]
        [run("rm -rf ./{}".format(item)) for item in archs]
