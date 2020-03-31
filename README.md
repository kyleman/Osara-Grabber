# Osara-Grabber
An automatic installer for the [Osara Reaper scripts](https://github.com/jcsteh/osara) on MacOS

# Downloading

## Release Builds
Current version v 1.1 03/30/2020.
[Download the Osara Grabber here](https://github.com/kyleman/Osara-Grabber/releases/latest).

## Prerelease Builds
To get the code as it stands currently.
Note: you must have git installed for this to work.
`git clone https://github.com/kyleman/Osara-Grabber.git`

# Using Osara Grabber

## in finder with the GUI
After downloading, Unzip the zip file. Run Osara_Grabber.command. If MacOS warns you about not being able to run it, try running it by pressing capslock + shift + control + m. Then click on open in the menu that should pop up.

## from terminal
If you cloned the repo, change directories to the Osara Grabber directory and run `./Osara_Grabber.command`.
By default if you don't specify a directory as the first argument, the Osara dylib and keymap files will be copied to your reaper'- resource path into UserPlugins and KeyMaps folders respectively. If you do provide a path like ""/Volumes/MyThumbDrive/ReaperPortable", the dylib and keymap file will be placed there instead.
note: it is good practice to always wrap your paths in quotes.

# Changes

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
* I have personally only tested this with MacOS 10.15.4 Catalina. While it should work an other versions of MacOS, that is untested territory.

# FAQ
Q: Is there a Windows version?

A: Not as of yet.

Q: I want ABC or XYZ feature?

A: Open an issue and lets chat.