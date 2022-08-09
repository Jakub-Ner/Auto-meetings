#!/bin/bash
#
chmod +xwr ./CONST.sh
source CONST.sh
#
echo -e " Cleaning before installing:\n"
chmod +x ./uninstall.sh
sudo ./uninstall.sh
#
echo -e "\n Creating user auto-meetings:\n"
sudo useradd ${NAME}
#
#
echo -e "\n Protection for credentials:\n"
sudo echo -e 'PASS=""\nMY_MAIL=""' > ${TOP_SECRET_DIR}
sudo chmod 700 ${TOP_SECRET_DIR}
sudo setfacl -m u:${NAME}:rwx ${TOP_SECRET_DIR}
#
sudo chown root:root $(pwd)/auth.sh
sudo chmod 106 $(pwd)/auth.sh
#
sudo chown root:root $(pwd)/sleep.sh
sudo chmod 106 $(pwd)/sleep.sh
#
sudo echo "auto-meetings ALL=(ALL) NOPASSWD: /bin/bash $(pwd)/auth.sh" > /etc/sudoers.d/${NAME}
sudo echo "Cmnd_Alias SLEEP = /usr/sbin/rtcwake -u -m mem -s *" | tee -a /etc/sudoers.d/${NAME}
sudo echo "auto-meetings ALL=(ALL) NOPASSWD: SLEEP" | tee -a /etc/sudoers.d/${NAME}
#
#
echo -e "\n Setting up auto-meetings as a systemd service:\n"
echo -e "Copy path displayed below and paste it to the appropriate place in automeetings.service file:\n"
echo $(pwd)/../main.py
echo -e "\nIf You have set path click ENTER.\n"
read OK
sudo cp $(pwd)/automeetings.service /etc/systemd/system/automeetings.service
systemctl daemon-reload
systemctl enable automeetings
systemctl start automeetings
#
#
echo -e "\n Adding auto-meetings alias:\n"
sudo echo 'alias auto-meetings="xdg-open http://127.0.0.1:5000/"' | sudo tee -a ~/.bash_aliases > /dev/null
chmod +220 ~/.bash_aliases # in case file was created during the script
source ~/.bashrc