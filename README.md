# Osara-Grabber
An automatic installer for the [Osara Reaper scripts](https://github.com/jcsteh/osara).

# Downloading

## Standard Binary Releases
Current version v 2.1 08/26/2020.
[Download Osara Grabber here](https://github.com/kyleman/Osara-Grabber/releases/latest).

## Live code as it stands
To get the code as it stands currently, run the following commands.
Note: you must have git and a working python3 install for this to work. Setting these up are beyond the scope of the readme
```
pip3 install requests
git clone https://github.com/kyleman/Osara-Grabber.git
cd Osara-Grabber
python3 Osara_Grabber.py
```

# Using Osara Grabber

## in MacOS Finder 
Unzip Osara_Grabber_MacOS.zip and run Osara_Grabber.
If MacOS prevents you from running the file, control click the file and press open in the menu. For VoiceOver users, control clicking is the same as VoiceOver + shift + control + m. In this case VoiceOver has to be the capslock key.

## MacOS Terminal
On MacOS by default if you don't specify a directory as the first argument, the Osara dylib and key-map files will be copied to your reaper'- resource path into UserPlugins and KeyMaps folders respectively. If you do provide a path like "/Volumes/MyThumbDrive/ReaperPortable", the dylib and key-map file will be placed there instead.

## in Windows file Explorer
Unzip Osara_Grabber_Windows.zip and run Osara_Grabber.exe. You then complete the install process in the Osara installer.

# Changes
## v2.1
* MacOS: fix a bug in paths when trying to specify a directory on the terminal
* MacOS: fix variable error when copying the key-map
* README: clean up the readme

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
* Added the ability to install the key-map.
* Switched from running the prebuilt .command files in the dmg to copying the files directly.

## v1.0 *initial release)
* First working release. See above for details.

# Current limitations
* On MacOS you con't specify a portable install of reaper unless you run Osara_GRabber from the command-line.

# FAQ
Q: What operating systems are supported?
A: As of v2.0 08/13/2020 both MacOS and windows are supported.

Q: Will this auto update Osara?
A: No. when a new version of Osara get released you still must manually run Osara Grabber. Osara Grabber is just to automate the install process.

Q: I want ABC or XYZ feature?
A: Open an issue and lets chat.