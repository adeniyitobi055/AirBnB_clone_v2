#!/usr/bin/python3
"""
2-do_deploy_web_static module
"""
from fabric.api import env, put, run
from datetime import datetime
from os import path


env.hosts = ['52.87.215.57', '34.229.49.137']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    try:
        if not (path.exists(archive_path)):
            return False

        # upload the archive to the tmp directory
        put(archive_path, '/tmp/')

        # create target directory
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'
            .format(timestamp))

        # uncompress the archive and delete .tgz
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
            /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # remove archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # move content into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
            /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # remove irrelevant web_static dir
        run('sudo rm -rf /data/web_static/releases/\
            web_static_{}/web_static'.format(timestamp))

        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-establish sym link
        run('sudo ln -s /data/web_static/releases/web_static_{}/ \
            /data/web_static/current'.format(timestamp))
        return True

    except Exception:
        return False
