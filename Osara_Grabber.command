BASE_URL="https://osara.reaperaccessibility.com/snapshots/"
INSTALL_OSARA="Install OSARA extension.command"

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
INSTALL_CMD="$MOUNT_POINT/$INSTALL_OSARA"

"$INSTALL_CMD"

echo "ejecting $OSARA_FILE"
hdiutil detach "$MOUNT_POINT" > /dev/null
rm -f "$OSARA_FILE"