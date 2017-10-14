#!/usr/bin/env python

import subprocess


#checks what is in plexversion this is used to check if we have the newest version
checkVersion = subprocess.getoutput(["ls plexversion/"])
print (checkVersion)
#used for the download this is variable changes
linkVar = "1.9.4.4325-1bf240a65/"
#plex is the website 
plex = 'https://downloads.plex.tv/plex-media-server/'
#version is the version needed for download
version = 'plexmediaserver_1.9.4.4325-1bf240a65_i386.deb' 
#full link is
fullLink = plex + linkVar + version

#newIdea = subprocess.run(["wget", "-r", "l1", "--no-parent", "-Ai386.deb", "https://www.plex.tv/downloads/", "-O", "*i386.deb", "-P", "/home/server/Plex-folder/plexversion"])

#print (newIdea)

if checkVersion == version:
	print("Plex is up to date")
else:	# Download the newest version and install
	subprocess.run(["wget", fullLink, "-P", "/home/server/Plex-folder/plexversion"])
	subprocess.run(["sudo", "dpkg", "-i", "/home/server/Plex-folder/plexversion/" + version])
	oke = input('do you want to reboot [Y/n]: ')
	if oke == 'n':
		print("Will be updated on reboot")
	else:
		subprocess.run(["sudo", "reboot"])
