from pathlib import Path
import os
import sys
import re
import urllib.request
import requests
import subprocess as sp

#constants
base_url = "https://osara.reaperaccessibility.com/snapshots/"
home = Path.home()
osara_webpage = requests.get(base_url).text # str of the osara webpage
version = 3.0 #current version of osara grabber

def yaynay(prompt: str, true = "y", false = "n") -> bool:
 """yaynay will ask the user for there response to a question with a binary answer. Loops until true or false is matched.
 returns a boolean based on the matched answer.
 prompt is the str of the question you want ta ask (required)
 true is the true answer you want to match (defaults to "t")
 false is the false answer you want to match (defaults to "f")
 example:
 if yaynay("Is it raining?"):
  print("bring your umbrella")
 else:
  print("Okay. no umbrella for today.")
 """
 while True:
  answer = input("{0} {1} / {2} ".format(prompt, true, false))
  if answer ==true:
   return True
  elif answer == false:
   return False

def getInstallerName(type: str) -> str:
 print("Looking for file")
 installer = re.compile("osara_.*\.{0}".format(type))
 installer_name = installer.search(osara_webpage).group()
 return installer_name

def getFullURL(installer_name: str) -> str:
 dl = re.compile("https://.*/{0}".format(installer_name))
 full_url = dl.search(osara_webpage).group()
 return full_url

def downloadInstaller(url: str, file_name: str) -> None:
 response = urllib.request.urlopen(url)
 with open(file_name, 'b+w') as file:
  file.write(response.read())

if sys.platform == "darwin":
 osara_dylib = Path(".data/reaper_osara.dylib")
 osara_keymap = Path(".data/OSARA.ReaperKeyMap")
 
 try:
  dylib_install_path = Path(sys.argv[1]) / "UserPlugins"
 except IndexError:
  dylib_install_path = home / "Library/Application Support/reaper/UserPlugins/"

 try:
  keymap_install_path = Path(sys.argv[1]) / "KeyMaps"
 except IndexError:
  keymap_install_path = home / "Library/Application Support/reaper/KeyMaps/"

 dmg_name = getInstallerName("dmg") 
 
 print("Downloading: {0}".format(dmg_name))

 full_url = getFullURL(dmg_name)

 downloadInstaller(full_url, dmg_name)

 if os.path.exists(dmg_name):
  os.system("hdiutil attach -mountpoint ./osara ./" + dmg_name + " > /dev/null")

  print("cp osara/{0} '{1}'".format(osara_dylib, dylib_install_path))
  os.system("cp osara/{0} '{1}'".format(osara_dylib, dylib_install_path))

  if yaynay("Do you want to install the keymap? If this is your first install of Osara, you should say yes: "):
   print("cp osara/{0} '{1}'".format(osara_keymap, keymap_install_path))
   os.system("cp osara/{0} '{1}'".format(osara_keymap, keymap_install_path))

  print("ejecting {0}".format(dmg_name))
  os.system("hdiutil detach osara > /dev/null")

  print("deleting {0}".format(dmg_name))
  os.remove(dmg_name)

 else:
  print("{0} can't be found.".format(dmg_name))

elif sys.platform == "win32":
 osara_dll32 = Path("UserPlugins/reaper_osara32.dll")
 osara_dll64 = Path("UserPlugins\reaper_osara64.dll")
 osara_keymap = "KeyMaps\reaper_osara64.dll"
 
 try:
  dll_install_path = Path(sys.argv[1]) + "UserPlugins"
 except IndexError:
   dll_install_path = home /"AppData/Roaming/REAPER/UserPlugins/"

 try:
  keymap_install_path = Path(sys.argv[1] + "KeyMaps")
 except IndexError:
  keymap_install_path = home / "AppData/Roaming/REAPER/KeyMaps/"

 exe_name = getInstallerName("exe")

 print("Downloading: {0}".format(exe_name))

 full_url = getFullURL(exe_name)

 downloadInstaller(full_url, exe_name)

 if os.path.exists(exe_name):
  try:
   sp.check_output([exe_name])
  except sp.CalledProcessError as cpe:
   print("Installer failed to run")
  print("deleting {0}".format(exe_name))
  os.remove(exe_name)
 else:
  print("{0} can't be found.".format(exe_name))

else:
 print("Not supported OS!\nPlease run this on a supported version of MacOS or Windows.")
 sys.exit(0)

