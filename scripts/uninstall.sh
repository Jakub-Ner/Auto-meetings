#!/bin/bash
#
SCRIPT=$(readlink -f "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")
#
sudo rm /etc/systemd/system/auto-meetings.service
systemctl daemon-reload
systemctl disable automeetings
systemctl stop automeetings
#
sudo userdel auto-meetings
#
sudo rm ${SCRIPT_PATH}/auto-meetings
sudo rm ${SCRIPT_PATH}/auto-meetings.service
sudo rm ${SCRIPT_PATH}/../browser/TOP_SECRET.py
sudo rm /etc/sudoers.d/auto-meetings
