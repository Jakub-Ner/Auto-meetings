import shlex
open_page = "xdg-open "
open_obs = shlex.split("obs-studio --startrecording &>/dev/null")
close_obs = shlex.split("pkill -f -9 obs-studio")
start_sleep = shlex.split('sudo /usr/sbin/rtcwake -u -m mem -s ')
