#!/usr/bin/python

import os
import sys

args = sys.argv

torrentid = args[0]
torrentname = args[1]
torrentrootpath = args[2]


# These file types will not be linked
excluded_extensions = ['.png', '.nfo', '.jpg', '.txt']

# These prefixed will be removed from the link, the link will still be made though!
unwanted_prefixes = ['aaf-']

# These dirs are skipped
unwanted_dirs = ['Sample']

# Needs to exist, needs to be on the same partition as the torrentfolder!
destinationfolder = '/example/path/without/trailing/slash'

# Only use for torrent folders ending in one of these folders:
trackers = ['btn']


####### - Do stuff

def remove_prefix(name):
    for prefix in unwanted_prefixes:
        if name.startswith(prefix):
            return name.replace(prefix, '', 1)
    return name


# Only do stuff if the torrent is saved to one of the completed folders we want
if os.path.split(torrentrootpath)[1] in trackers:
    torrentpath = os.path.join(torrentrootpath, torrentname)

    if os.path.isdir(torrentpath):
        for root, dirs, files in os.walk(torrentpath):
            for unwanted in unwanted_dirs:
                if unwanted in dirs:
                    dirs.remove(unwanted)
            for name in files:
                ext = os.path.splitext(name)[1]
                if ext not in excluded_extensions:
                    sourcepath = os.path.join(root, name)

                    name = remove_prefix(name)

                    destinationpath = os.path.join(destinationfolder, name)

                    os.link(sourcepath, destinationpath)
    else:
        torrentname = remove_prefix(torrentname)
        destinationpath = os.path.join(destinationfolder, torrentname)
        os.link(torrentpath, destinationpath)
