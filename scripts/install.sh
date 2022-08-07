#!/bin/bash

chmod +xwr ./CONST.sh
source CONST.sh

echo -e " Cleaning before installing:\n"
chmod +x ./uninstall.sh
sudo ./uninstall.sh

echo -e "\n Creating user auto-meetings:\n"
sudo useradd ${NAME}
#sudo passwd ${NAME}

echo -e "\n Protection for credentials:\n"
sudo touch ${TOP_SECRET_DIR}
sudo setfacl -m u:${NAME}:rwx ${TOP_SECRET_DIR}

sudo chown root:root $(pwd)/auth.sh
sudo chmod 106 $(pwd)/auth.sh
sudo echo "auto-meetings ALL=(ALL) NOPASSWD: $(pwd)/auth.sh" > /etc/sudoers.d/${NAME}


echo -e "\n Adding auto-meetings alias:\n"
sudo echo 'alias auto-meetings="xdg-open http://127.0.0.1:5000/"' | sudo tee -a ~/.bash_aliases > /dev/null
chmod +220 ~/.bash_aliases # in case file was created during the script
source ~/.bashrc
