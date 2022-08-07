#!/bin/bash
source CONST.sh
#
sudo userdel ${NAME}
sudo rm /etc/sudoers.d/${NAME}
sudo rm ${TOP_SECRET_DIR}
unalias ${NAME}