#include <stdlib.h>
#include <iostream>
#include <chrono>
#include <thread>
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
void run_meeting(){
    // start meeting
    std::string command = "xdg-open " + link;
    system(command.c_str());

    // record if RECORD_SETTING is "11" or "1"
    if (RECORD_SETTING[0] == '1')
        system("obs-studio --startrecording");

    // wait 2 hours <- to improve
    std::this_thread::sleep_for(std::chrono::hours (2));

    // finish recording
    if (RECORD_SETTING[0] == '1')


}

void wait_for_meeting() {
    std::ifstream fin;
    fin.open("variables/next_meeting.txt");

    // if file exist and is not empty:
    if (fin && fin.peek() != std::ifstream::traits_type::eof()) {
        std::string name;
        tm meeting_time;

        fin >> name;

        fin >> meeting_time.tm_mday;

        fin >> meeting_time.tm_mon;
        meeting_time.tm_mon--; // cause tm_mon is from 0-11

        fin >> meeting_time.tm_year;
        meeting_time.tm_year -= 1900; // cause tm_year is since 1900

        char colon;
        fin >> meeting_time.tm_hour;
        fin >> colon;

        fin >> meeting_time.tm_min;

        getline(fin, link);

        menu(name, meeting_time);
    }
}

void menu(const std::string &name, tm& meeting_time){
    std::string time_to_display = asctime(&meeting_time);

    // at the end of time_to_display appear default weekday, so cut it
    std::cout << "\n" << name << " starts at: " << time_to_display.substr(3) << "\n";

    int waiting_time;
    do {
        waiting_time = time_to_wait(meeting_time);

        if (waiting_time < 60 * 60 * 24) {
            std::cout << "time to wait: " << waiting_time << '\n';
            std::this_thread::sleep_for(std::chrono::minutes(4));

        }else {
            std::cout << "You have not any meeting within next 24h. Have a great day!\n";
            std::this_thread::sleep_for(std::chrono::hours(1));
        }
    }while(waiting_time > 6*60*60); // the loop finishes 2-6 minutes before meeting
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

