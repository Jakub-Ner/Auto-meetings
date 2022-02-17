#include <stdlib.h>
#include <iostream>
#include <cstring>
#include <fstream>
#include "options.h"
#include "main.h"
#include "variables/test_mode.h"
#include "JSON.h"
#include "my_time.h"

std::string RECORD_SETTING = "11";
bool SLEEP_SETTING = false;

int main(int argc, char *argv[]) {
#ifdef test_mode
    test();
#else
//    JSON().check_json_correctness();
    if(argc > 1 ){
        choose_option(argc, argv);
    }
    system("./get_links.sh"); // for now it is default
#endif //test_mode
    wait_for_meeting();
//    system("obs-studio --startrecording");
    return 0;


}
void wait_for_meeting() {
    std::ifstream fin;
    fin.open("variables/next_meeting.txt");

    // if file exist and is not empty:
    if (fin && fin.peek() != std::ifstream::traits_type::eof()) {
        std::string name;
        fin>>name;

        tm meeting_time;
        fin>>meeting_time.tm_mday;

        fin>>meeting_time.tm_mon;
        meeting_time.tm_mon--; // cause tm_mon is from 0-11

        fin>>meeting_time.tm_year;
        meeting_time.tm_year -= 1900; // cause tm_year is since 1900

        char colon;
        fin>>meeting_time.tm_hour;
        fin>>colon;

        fin>>meeting_time.tm_min;

        std::string time_to_display = asctime(&meeting_time);
    // at the end of time_to_display appear default weekday, so cut it
        std::cout<<"\n"<<name<<" starts at: "<<time_to_display.substr(3)<<"\n";
        time_to_wait(meeting_time);
    }
}

void choose_option(int argc, char *argv[]) {
    if (strcmp(argv[1], "--help") == 0) help();
    if (strcmp(argv[1], "--sleep") == 0) SLEEP_SETTING = sleep(10); // <- mocking time_to_sleep
    if (strcmp(argv[1], "--record") == 0) record();
    if (argc == 4) {
        if (strcmp(argv[1], "--add") == 0) add_meeting(argv[2], argv[3]);
    }
}

void test() {
//    add_meeting("https://pwr-edu.zoom.us/j/95359922014?pwd=S0Z2c0w3L0pZSTVtNzJqZTJFQkIrQT09", "12:35 16-02-2022");
}

