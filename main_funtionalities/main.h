#ifndef AUTOMATION_OF_STUDIES_MAIN_H
#define AUTOMATION_OF_STUDIES_MAIN_H

std::string link;
std::string name;

void wait_for_meeting();
void load_settings();
void run_meeting();
void choose_option(int argc, char *argv[]);
void menu(const std::string &name, tm& meeting_time);

void test();

#endif //AUTOMATION_OF_STUDIES_MAIN_H
