#ifndef AUTOMATION_OF_STUDIES_WINDOWS_H
#define AUTOMATION_OF_STUDIES_WINDOWS_H
#include <iostream>

const std::string open_page = "start ";
const std::string open_obs = "c: & cd \"C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe\" --startrecording";
const std::string get_meetings = "get_links.bat";
const std::string start_sleep[] = {"currently ", " unavailable"};
//const std::string start_sleep[] = {"runas rctwake -u -s ", "%windir%\\System32\\rundll32.exe powrprof.dll,SetSuspendState 0,1,0"};
const std::string close_obs = "taskkill /IM \"obs64.exe\" /F";

#endif //AUTOMATION_OF_STUDIES_WINDOWS_H
