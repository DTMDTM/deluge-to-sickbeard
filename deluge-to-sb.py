#!/usr/bin/python

import os
import sys

args = sys.argv

torrentid = args[1]
torrentname = args[2]
torrentrootpath = args[3]


# These file types will not be linked
excluded_extensions = ['.png', '.nfo', '.jpg', '.txt']

# These prefixed will be removed from the link, the link will still be made though!
unwanted_prefixes = ['aaf-']

# These dirs are skipped
unwanted_dirs = ['Sample']

# Only use for torrent folders ending in one of these foldernames
# For example, if Deluge would put torrents from btn in /example/path/torrent/completed/btn
# and torrents from passthepopcorn in /exampe/path/torrent/completed/ptp, 
# you can use the following config. Achieve the above-mentioned paths by using the labels plugin 
# in Deluge.
trackers = ['btn', 'ptp'] # EDIT ME

# Map torrent folders to processing directories; first entry here goes to first entry in 
# trackers above, etc.
destinations = ['/example/path/torrent/completed/sickbeard_processing',\
                '/example/path/torrent/completed/couchpotato_processing'] # EDIT ME

# Merge the trackers and destinations
destination_dict = dict(zip(trackers, destinations))


####### - Do stuff

def remove_prefix(name):
    for prefix in unwanted_prefixes:
        if name.startswith(prefix):
            return name.replace(prefix, '', 1)
    return name


if torrentrootpath[-1:] == "/":
    torrentrootpath = torrentrootpath[0:-1]

tracker = os.path.split(torrentrootpath)[1] 
# Only do stuff if the torrent is saved to one of the completed folders we want
if tracker in trackers:
    torrentpath = os.path.join(torrentrootpath, torrentname)
    
    # If the torrent contains a dir, process it
    if os.path.isdir(torrentpath):
        for root, dirs, files in os.walk(torrentpath):
            # Remove unwanted stuff
            for unwanted in unwanted_dirs:
                if unwanted in dirs:
                    dirs.remove(unwanted)

            for name in files:
                # Check if the current file is not an excluded filetype
                ext = os.path.splitext(name)[1]
                if ext not in excluded_extensions:
                    sourcepath = os.path.join(root, name)

                    name = remove_prefix(name)

                    destinationpath = os.path.join(destination_dict[tracker], name)

                    os.link(sourcepath, destinationpath)
    else:
        # Torrent is a single file, no processing needed.
        # Note that if the torrent contains a single file, it is assumed it is not one of the
        # excluded file types as defined in excluded_extensions.
        torrentname = remove_prefix(torrentname)
        destinationpath = os.path.join(destination_dict[tracker], torrentname)
        os.link(torrentpath, destinationpath)
