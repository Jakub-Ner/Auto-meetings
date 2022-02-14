#ifndef AUTOMATION_OF_STUDIES_OPTIONS_H
#define AUTOMATION_OF_STUDIES_OPTIONS_H

bool help();
//bool menu();

bool add_meeting(std::string &args1, std::string &args2);
bool validate(const std::string& date); // <- it should be improved
bool sleep(int time_to_sleep);
void record();

#endif //AUTOMATION_OF_STUDIES_OPTIONS_H
