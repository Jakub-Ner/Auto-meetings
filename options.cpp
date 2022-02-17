#include <string>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include "options.h"
#include "variables/test_mode.h"
#include "JSON.h"


void help() {
    std::cout << R"(Welcome in Auto-meetings!
This program helps dealing with remote meetings.

OPTIONS
    -a, --add "link" "date" Set new meeting. Give: link to meetings in "", date in format: "hh:mm DD-MM-YYYY"
    -s, --sleep             Sleep PC until next meeting. Then turn on the meeting. After meeting sleep again...
    -r, --record            Set you recording preferences
)";
}

void add_meeting(const std::string &link, std::string date) {
    while (!validate(date)) {
        std::cout << "incorrect format of the date. Should be: hh-mm DD-MM-YYYY\n for example \"12:58 27-01-2023\"\n";
        std::cin >> date;
    }
#ifdef test_mode
#else
    std::cout << "Do you want to try if link works?[y/n] ";
    std::string input;
    std::cin >> input;
    if (input == "y") {
        std::string command = "xdg-open " + link;
        system(command.c_str());
    }
#endif //test_mode
    JSON().save_meeting(link, date);
}


bool validate(const std::string &date) {
    if (date.size() != 16) return false; // "hh:mm DD-MM-YYYY".size() = 16

    std::string hour = date.substr(0, 2);
    std::string minute = date.substr(3, 2);

    std::string day = date.substr(6, 2);
    std::string month = date.substr(9, 2);
    std::string year = date.substr(12, 4);

    if (minute > "59" && minute < "00") return false;
    if (hour > "23" && hour < "00") return false;

    if (day > "31" && day < "01") return false; // months length differs
    if (month > "12" && month < "01") return false;
    if (year < "2022") return false;

    return true;
}


void record() {
    std::string n;

    std::ofstream fout;
    fout.open("variables/RECORD_SETTING.txt");

    std::cout << R"(
11 - if you want to set meetings recording as default.
00 - if you want to disable meetings recording as default.
1  - if you want to record next meeting.
 )";

    std::cin >> n;
    if (n == "11") {
        std::cout << "You have set meetings recording as default.\n";
        fout << "11";

    } else if (n == "00") {
        std::cout << "You have disabled meetings recording as default";
        fout << "00";

    } else if (n == "1") {
        std::cout << "You will record your next meeting";
        fout << "1";

    } else std::cout << "Incorrect input! You could not set your recording preferences.";
    fout.close();
}