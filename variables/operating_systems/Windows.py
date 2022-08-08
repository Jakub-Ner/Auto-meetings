# TODO: create version for Windows
open_page = "start "
open_obs = f"c: & cd \"C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe\" --startrecording"
get_meetings = "get_links.bat"
# start_sleep = ["currently ", " unavailable"]
# start_sleep = {"runas rctwake -u -s ", "%windir%\\System32\\rundll32.exe powrprof.dll,SetSuspendState 0,1,0"}
close_obs = f"taskkill /IM \"obs64.exe\" /F"