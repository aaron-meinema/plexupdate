#!/usr/bin/env python

import subprocess

myHome = ("/home/" + subprocess.getoutput("whoami"))

#checks what is in plexversion this is used to check if we have the newest version
checkVersion = subprocess.getoutput('ls ~/plexupdate/plexversion/')
#used for the download this is variable changes
linkVar = "1.9.4.4325-1bf240a65/"
#plex is the website 
plex = 'https://downloads.plex.tv/plex-media-server/'
#version is the version needed for download
version = 'plexmediaserver_1.9.4.4325-1bf240a65_i386.deb' 
#full link is
fullLink = plex + linkVar + version
print (checkVersion)

if checkVersion == version:
    print("Plex is up to date")
else:	# Download the newest version and install
    subprocess.run(['mv', myHome + '/plexupdate/plexversion/' + checkVersion, myHome + "/plexupdate/oldversions/"])
    subprocess.run(["wget", fullLink, "-P", myHome + "/plexupdate/plexversion"])
    subprocess.run(["sudo", "dpkg", "-i", myHome + "/plexupdate/plexversion/" + version])
    oke = input('do you want to reboot [Y/n]: ')
    if oke == 'n' || oke == 'N':
        print("Will be updated on reboot")
    else:
        subprocess.run(["sudo", "reboot"])
