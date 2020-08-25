# Osara-Grabber
An automatic installer for the [Osara Reaper scripts](https://github.com/jcsteh/osara).

# Downloading

## Standard Binary Releases
Current version v 2.0 08/24/2020.
[Download Osara Grabber here](https://github.com/kyleman/Osara-Grabber/releases/latest).

## Live code as it stands
To get the code as it stands currently, run the following commands.
Note: you must have git and a working python3 install for this to work. Setting these up are beyond the scope of the readme
````
pip3 install requests
git clone https://github.com/kyleman/Osara-Grabber.git
cd Osara-Grabber
python3 Osara_Grabber.py
```

# Using Osara Grabber

## in the MacOS Finder 
Unzip Osara_Grabber_MacOS.zip and run Osara_Grabber.
If MacOS prevents you from running the file, control click the file and press open in the menu. For VoiceOver users, control clicking is the same as VoiceOver + shift + control + m. In this case VoiceOver has to be the capslock key.

## in Windows file Explorer
Unzip Osara_Grabber_Windows.zip and run Osara_Grabber.exe.

## from commandline
If you cloned the repo, change directories to the Osara Grabber directory and run `python3 Osara_Grabber.py`
On MacOS by default if you don't specify a directory as the first argument, the Osara dylib and keymap files will be copied to your reaper'- resource path into UserPlugins and KeyMaps folders respectively. If you do provide a path like ""/Volumes/MyThumbDrive/ReaperPortable", the dylib and keymap file will be placed there instead.
On Windows this is handled by the installer.
note: it is good practice to always wrap your paths in quotes.

# Changes
## v2.0
* Osara Grabber is all knew and supports Windows and MacOS
* Update the readme to reflect the new use of python and its cross-platform nature
* port older bash shell script to python for MacOS
* implement Windows support

## v1.2
* Added this change-log.
* Fixed a spelling mistake in the README.

##v1.1
* Added the ability to change the install location by passing a directory on the command-line.
* Added the ability to install the keymap.
* Switched from running the prebuilt .command files in the dmg to copying the files directly.

## v1.0 *initial release)
* First working release. See above for details.

# Current limitations
* On MacOS you con't specify a portible install of reaper unless you run Osara_GRabber from the commandline.

# FAQ
Q: What operating systems are supported?
A: As of v2.0 08/13/2020 both MacOS and windows are supported.

Q: Will this auto update Osara?
A: No. when a new version of Osara get released you still must manually run Osara Grabber. Osara Grabber is just to autimate the install process.

Q: I want ABC or XYZ feature?
A: Open an issue and lets chat.