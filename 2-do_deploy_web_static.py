#!/usr/bin/python3
"""
    Distributing an archive to the web servers.
"""
from os import path
from fabric.api import run, put, env

env.hosts = ['54.236.53.229', '18.204.7.180']


def do_deploy(archive_path):
    """Distributes the archive to the servers
    Args:
        archive_path (str): the path of the archive to deploy on the servers.
    """

    try:
        if not path.exists(archive_path):
            raise FileNotFoundError

        arc_path = archive_path.split("/")[-1]
        arc = arc_path.split(".")[0]

        remote = "/data/web_static/releases"
        dest = "{}/{}".format(remote, arc)

        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(dest))
        run('tar -xzf /tmp/{} -C {}'.format(arc_path, dest))
        run('rm /tmp/{}'.format(arc_path))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(dest))

    except:
        print("Error. Version deploy aborted")
        return False

    print("New version deployed!")
    return True
