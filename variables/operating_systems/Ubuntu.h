#ifndef AUTOMATION_OF_STUDIES_UBUNTU_H
#define AUTOMATION_OF_STUDIES_UBUNTU_H

#include <iostream>

const std::string open_page = "xdg-open ";
const std::string open_obs = "obs-studio --startrecording";
const std::string close_obs = "pkill -f -9 obs-studio";
const std::string get_meetings = "./get_links.sh";
const std::string start_sleep[] = {"sudo rtcwake -u -s ", " -m mem"};


#endif //AUTOMATION_OF_STUDIES_UBUNTU_H
