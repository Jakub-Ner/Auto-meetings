#ifndef AUTOMATION_OF_STUDIES_OPTIONS_H
#define AUTOMATION_OF_STUDIES_OPTIONS_H

void add_meeting(const std::string &link, std::string date);

void help();

void record();

bool sleep(int time_to_sleep);


bool save_meeting(const std::string &link, const std::string &date);

bool validate(const std::string &date); // <- it should be improved

#endif //AUTOMATION_OF_STUDIES_OPTIONS_H
