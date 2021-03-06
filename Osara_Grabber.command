BASE_URL="https://osara.reaperaccessibility.com/snapshots/"
DYLIB=".data/reaper_osara.dylib"
KEYMAP=".data/OSARA.ReaperKeyMap"

if [ -z "$1" ]
then
 DYLIB_INSTALL_PATH="$HOME/Library/Application Support/REAPER/UserPlugins"
 KEYMAP_INSTALL_PATH="$HOME/Library/Application Support/REAPER/KeyMaps"
else
 DYLIB_INSTALL_PATH="$1"
 KEYMAP_INSTALL_PATH="$1"
fi

echo "Looking for file"
curl -sL "$BASE_URL" -o snapshot.txt > /dev/null
OSARA_FILE=$(egrep -o "osara_.*\.dmg" snapshot.txt)
rm snapshot.txt

DOWNLOAD_URL=$BASE_URL$OSARA_FILE

echo "downloading $OSARA_FILE"
curl -sO "$DOWNLOAD_URL" > /dev/null

echo "mounting $OSARA_FILE"
hdiutil mount "./$OSARA_FILE" > /dev/null
MOUNT_POINT="$(hdiutil info | egrep -o "/Volumes/OSARA .*")"

cp "$MOUNT_POINT/$DYLIB" "$DYLIB_INSTALL_PATH"
echo "copied $MOUNT_POINT/$DYLIB to $DYLIB_INSTALL_PATH"

read -p "Do you want to install the keymap? If this is your first install of Osara, you should say yes. <y/n> " prompt
if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]
then
 cp "$MOUNT_POINT/$KEYMAP" "$KEYMAP_INSTALL_PATH"
 echo "copied $MOUNT_POINT/$KEYMAP to $KEYMAP_INSTALL_PATH"
  fi

echo "ejecting $OSARA_FILE"
hdiutil detach "$MOUNT_POINT" > /dev/null
rm -f "$OSARA_FILE"