#include <stdlib.h>
#include <iostream>
#include <chrono>
#include <thread>
#include <cstring>
#include <fstream>
#include <sstream>

#include "../variables/GLOBAL.h"
#include "main.h"
#include "options.h"
#include "JSON.h"
#include "my_time.h"

std::string RECORD_SETTING = "11";
bool SLEEP_SETTING = false;

int main(int argc, char *argv[]) {
#ifdef test_mode
    test();
#else
    //    JSON().check_json_correctness();
    if (argc > 1) {
        choose_option(argc, argv);
    }

    // use CTRL+C to stop the program
    while (true) {
        system(get_meetings.c_str()); // for now, it is default
        load_settings();
#endif //test_mode
        wait_for_meeting();
        if (name != "@") {
            run_meeting();
        }
    }
}

void load_settings() {
    std::string temp;
    std::ifstream fin;
    fin.open("variables/RECORD_SETTING.txt");
    fin >> temp;
    fin.close();

    if (temp == "11" || temp == "00" || temp == "1")
        RECORD_SETTING = temp;

}

void run_meeting() {
    // start meeting
    std::string command = open_page + link;
    std::cout << command << "\n";
    system(command.c_str());
    std::this_thread::sleep_for(std::chrono::seconds(10));


    // record if RECORD_SETTING is "11" or "1"
    if (RECORD_SETTING[0] == '1') {
        std::thread obs_thread([]() {
            system(open_obs.c_str());
        });
        // record for 106 minutes then close obs and detach thread
        std::this_thread::sleep_for(std::chrono::minutes(106));
        system(close_obs.c_str());
        obs_thread.detach();

    } else {
        std::this_thread::sleep_for(std::chrono::hours(106));
    }

}

void sleep(int waiting_time) {
    std::stringstream ss;
    ss << (waiting_time);

    std::string command;
    ss >> command;

    command = start_sleep[0] + command + start_sleep[1];

    std::cout << "WARNING: In a moment computer will be hibernated and wake up after around "
              << (waiting_time) / 3595 // instead of 3600 because '/' rounds down
              << " hours" << '\n';
    std::this_thread::sleep_for(std::chrono::minutes(1));
    system(command.c_str());

}

void wait_for_meeting() {
    std::ifstream fin;
    fin.open("variables/next_meeting.txt");

    // if file exist and is not empty:
    if (fin && fin.peek() != std::ifstream::traits_type::eof()) {
        tm meeting_time;

        fin >> name;
        // name == "@" means that arent any meeting on the list
        if (name == "@") {
            std::cout << "You have not any meeting today. Have a great day!\n";
            std::this_thread::sleep_for(std::chrono::seconds(5));

            if (SLEEP_SETTING) {
                sleep(36000);
            } else {
                std::this_thread::sleep_for(std::chrono::hours(1));
            }
        } else {
            fin >> meeting_time.tm_mday;

            fin >> meeting_time.tm_mon;
            meeting_time.tm_mon--; // cause tm_mon is from 0-11

            fin >> meeting_time.tm_year;
            meeting_time.tm_year -= 1900; // cause tm_year is since 1900

            char colon;
            fin >> meeting_time.tm_hour;
            fin >> colon;

            fin >> meeting_time.tm_min;
            fin >> link;
            fin.close();

            menu(name, meeting_time);
        }
    }
}


void menu(const std::string &name, tm &meeting_time) {
    std::string time_to_display = asctime(&meeting_time);

    // at the end of time_to_display appear default weekday, so cut it
    std::cout << "\n" << name << " starts at: " << time_to_display.substr(3, 13) << "\n";
    std::this_thread::sleep_for(std::chrono::seconds(5));

    int waiting_time = time_to_wait(meeting_time); // in seconds

    // the loop finishes 2-6 minutes before meeting
    // abs(x) because if now is ex. 27.02 and the meeting is in new month waiting time would be wrong
    if (abs(waiting_time) > 60 * 60) {
        check_mail_again = true;
        if (abs(waiting_time) < 60 * 60 * 8) {
            std::cout << "time to wait: " << waiting_time / 60 << " minutes" << '\n';
            if (SLEEP_SETTING) sleep(abs(waiting_time) - 60 * 3);
            else std::this_thread::sleep_for(std::chrono::hours(1));

        } else {
            std::cout << "You have not any meeting at least for the next 8 hours. Have a great day!\n";
            if (SLEEP_SETTING) {
                sleep(3600*8);
            } else {
                std::this_thread::sleep_for(std::chrono::hours(1));
            }
        }
        waiting_time = time_to_wait(meeting_time);

    }
    while (waiting_time > 5 * 60) {
        if (SLEEP_SETTING)
            sleep(waiting_time - 3 * 60);

        // after sleeping determine waiting_time
        waiting_time = time_to_wait(meeting_time);
    }

}



void choose_option(int argc, char *argv[]) {
    if (strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0) help();

    else if (strcmp(argv[1], "--sleep") == 0 || strcmp(argv[1], "-s") == 0) {
        std::cout << "sleeping is set to true\n";
        SLEEP_SETTING = true;

    } else if (strcmp(argv[1], "--record") == 0 || strcmp(argv[1], "-r") == 0) record();

    else if (argc == 4) {
        if (strcmp(argv[1], "--add") == 0 || strcmp(argv[1], "-a") == 0)
            add_meeting(argv[2], argv[3]);
        else std::cout << "Invalid parameters";

    } else std::cout << "Invalid parameters";

}

void test() {
//    add_meeting("https://pwr-edu.zoom.us/j/95359922014?pwd=S0Z2c0w3L0pZSTVtNzJqZTJFQkIrQT09", "12:35 16-02-2022");
}

