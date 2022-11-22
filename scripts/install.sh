#!/bin/bash
#
SCRIPT=$(readlink -f "$0")
SCRIPT_PATH=$(dirname "${SCRIPT}")
MAIN_PATH=$(
  builtin cd ${SCRIPT_PATH}/../
  pwd
)
#
function CREATE_SUDOERS() {
  echo "Cmnd_Alias SLEEP = /usr/sbin/rtcwake -u -m mem -s *" | tee -a ${SCRIPT_PATH}/auto-meetings &>/dev/null
  echo "auto-meetings ALL=(ALL) NOPASSWD: SLEEP" | tee -a ${SCRIPT_PATH}/auto-meetings &>/dev/null
}
function CREATE_UNIT_FILE() {
  UNIT_PATH=${SCRIPT_PATH}/auto-meetings.service

  echo "[Unit]" >${UNIT_PATH}
  echo "Description=Auto-meetings" | tee -a ${UNIT_PATH}
  echo "After=systemd-user-sessions.service" | tee -a ${UNIT_PATH}
  #
  echo "[Service]" | tee -a ${UNIT_PATH} &>/dev/null
  echo "User=auto-meetings" | tee -a ${UNIT_PATH} &>/dev/null
  echo "StandardOutput=journal" | tee -a ${UNIT_PATH} &>/dev/null
  echo "StandardError=journal" | tee -a ${UNIT_PATH} &>/dev/null
  echo "Restart=on-failure" | tee -a ${UNIT_PATH} &>/dev/null
  echo "RestartSec=10" | tee -a ${UNIT_PATH} &>/dev/null
  echo "KillMode=process" | tee -a ${UNIT_PATH} &>/dev/null
  echo "IgnoreSIGPIPE=no" | tee -a ${UNIT_PATH} &>/dev/null
  echo "RemainAfterExit=yes" | tee -a ${UNIT_PATH} &>/dev/null
  echo "RestartSec=10" | tee -a ${UNIT_PATH} &>/dev/null
  echo "Environment=DISPLAY=:0 XAUTHORITY=/home/jakubner/.Xauthority PYTHONPATH=${MAIN_PATH}" | tee -a ${UNIT_PATH} &>/dev/null
  echo "ExecStart=/bin/python3 -u ${MAIN_PATH}/main.py" | tee -a ${UNIT_PATH} &>/dev/null
  #
  echo "[Install]" | tee -a ${UNIT_PATH} &>/dev/null
  echo "WantedBy=multi-user.target" | tee -a ${UNIT_PATH} &>/dev/null
}
#
echo -e "\n Cleaning before installing:\n"
chmod +x ${SCRIPT_PATH}/uninstall.sh
${SCRIPT_PATH}/uninstall.sh
#
echo -e "\n Create symbol linking to .XAUTHORITY:\n"
/bin/bash -c 'ln -s -f "$XAUTHORITY" ~/.Xauthority'
#
echo -e "\n Installing python dependencies\n"
sudo -H pip install -r ${SCRIPT_PATH}/dependencies.txt
#
mkdir ${MAIN_PATH}/browser/credentials
#
#
echo -e "\n Setting up auto-meetings as a systemd service:\n"
CREATE_UNIT_FILE
sudo cp ${SCRIPT_PATH}/auto-meetings.service /etc/systemd/system/auto-meetings.service
systemctl daemon-reload
systemctl enable auto-meetings
systemctl start auto-meetings
#
#
echo -e "\n Adding auto-meetings alias:\n"
sudo echo 'alias auto-meetings="xdg-open http://127.0.0.1:5000/"' | sudo tee -a ~/.bash_aliases >/dev/null
chmod +220 ~/.bash_aliases # in case file was created during the script
. /home/jakubner/.bashrc
#
python3 ${MAIN_PATH}/browser/Auth.py
echo -e "\n Installation finished!\n"
#
