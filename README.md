deluge-to-sickbeard
============

Tool written in Python to link your downloaded torrents from deluge to sickbeard, 
to process in such a way that you can keep seeding.

So far only tested under linux with the same partition for the processing folder and the seeding folder.
The advantage of this is that you can use hard links which allow you to keep seeding the file as well as have it 
in your library. Using hard links also makes it possible to delete either the seeding file or the file in your lib
while not losing both. The third and foremost advantage is that using hardlinks is that you can have a copy that
you can rename while not storing the file twice, saving a lot of space!

The idea is that deluge-to-sb.py is called by deluge upon completion, using the execute-plugin. 
This will call the script with three arguments:

- The torrent ID (we discard this)
- The torrent name (identical to the filename if it's a single file, identical to the folder if it's a folder)
- The folder where the torrent is stored

Please open deluge-to-sb.py to edit the settings specific for your system, such as where your stuff should go
and for which trackers you want to use this.

This script works best if you have deluge setup to have labels for your series trackers (I use it with BTN)
and tell deluge to move those torrents to a specific folder. In this case you can have a folder, say 
/some/path/to/btn where deluge moves all your completed btn torrents. Since 'btn' is the lowest folder in that path
and 'btn' is in the 'trackers' list, the script will execute for btn-torrents - and only those.


