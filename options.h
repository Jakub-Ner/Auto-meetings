#ifndef AUTOMATION_OF_STUDIES_OPTIONS_H
#define AUTOMATION_OF_STUDIES_OPTIONS_H

void add_meeting(const std::string &link, std::string date);

void help();

void record();

bool validate(const std::string &date); // <- it should be improved

#endif //AUTOMATION_OF_STUDIES_OPTIONS_H
