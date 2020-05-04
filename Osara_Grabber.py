from pathlib import Path
import os
import sys
import re
import urllib.request
import requests
import subprocess

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

base_url = "https://osara.reaperaccessibility.com/snapshots/"
home = Path.home()

print("Looking for file")
r = requests.get(base_url).text

if sys.platform == "darwin":
 osara_dylib = Path(".data/reaper_osara.dylib")
 osara_kemap = Path(".data/OSARA.ReaperKeyMap")
 
 try:
  dylib_install_path = Path(sys.argv[1])
 except IndexError:
  dylib_install_path = home / "Library/Application Support/reaper/UserPlugins/"

 try:
  keymap_install_path = Path(sys.argv[1])
 except IndexError:
  keymap_install_path = home / "Library/Application Support/reaper/KeyMaps/"

 dmg = re.compile("osara_.*\.dmg")
 dmg_url = dmg.search(r).group()

 print("downloading {0}".format(dmg_url))
 full_url = base_url + dmg_url

 response = urllib.request.urlopen(full_url)
 with open(dmg_url, 'b+w') as dmg:
  dmg.write(response.read())

 if os.path.exists(dmg_url):
  os.system("hdiutil attach -mountpoint ./osara ./" + dmg_url + " > /dev/null")

 print("cp osara/{0} '{1}'".format(osara_dylib, dylib_install_path))
 os.system("cp osara/{0} '{1}'".format(osara_dylib, dylib_install_path))

 if yaynay("Do you want to install the keymap? If this is your first install of Osara, you should say yes: "):
  print("cp osara/{0} '{1}'".format(osara_keymap, keymap_install_path))
  os.system("cp osara/{0} '{1}'".format(osara_keymap, keymap_install_path))

 print("ejecting {0}".format(dmg_url))
 os.system("hdiutil detach osara > /dev/null")
 os.system("rm -f {0}".format(dmg_url))

elif sys.platform == "win32":
 osara_dll32 = Path("UserPlugins/reaper_osara32.dll")
 osara_dll64 = Path("UserPlugins\reaper_osara64.dll")
 keymap = "KeyMaps\reaper_osara64.dll"
 
 # set up windows install paths
else:
 print("Not supported OS!")
 sys.exit(0)

