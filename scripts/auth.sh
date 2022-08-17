#!/bin/bash
echo "set-up email"
#
SCRIPT=$(readlink -f "$0")
SCRIPT_PATH=$(dirname "${SCRIPT}")
MAIN_PATH=$(builtin cd ${SCRIPT_PATH}/../; pwd)
#
/usr/bin/gnome-terminal --tab --title="Set up credentials for Email" --command="bash -c 'sudo nano $MAIN_PATH/browser/TOP_SECRET.py; $SHELL'"