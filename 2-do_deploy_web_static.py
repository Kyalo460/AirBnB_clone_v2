#!/usr/bin/python3
"""distributes an archive to my web servers using the function do_deploy"""
from fabric.api import run, put, env
import os

env.hosts = ['52.3.251.52', '54.85.138.35']
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    deploys archive to web server
    """
    path = archive_path.split('/')[-1]
    line = path.split('.')[0]
    if not os.path.isfile(archive_path):
        return False
    if put(archive_path, "/tmp/{}".format(path)).failed:
        return False
    if run("sudo rm -rf /data/web_static/releases/{}"
            .format(line)).failed:
        return False
    if run("sudo mkdir -p /data/web_static/releases/{}/"
            .format(line)).failed:
        return False
    if run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(path, line)).failed:
        return False
    if run("sudo rm /tmp/{}".format(path)).failed:
        return False
    if run("sudo mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(line, line)).failed:
        return False
    if run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(line)).failed:
        return False
    if run("sudo rm -rf /data/web_static/current").failed:
        return False
    if run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(line)).failed:
        return False
    run("sudo systemctl restart nginx")

    return True
