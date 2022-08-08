#!/bin/bash
source CONST.sh
#
sudo rm /etc/systemd/system/automeetings.service
systemctl daemon-reload
systemctl disable automeetings
systemctl stop automeetings
#
sudo userdel ${NAME}
sudo rm /etc/sudoers.d/${NAME}
sudo rm ${TOP_SECRET_DIR}
unalias ${NAME}