#include <stdlib.h>
#include <iostream>
#include <cstring>
#include "options.h"
#include "main.h"
#include "variables/test_mode.h"
#include "JSON.h"

std::string RECORD_SETTING = "11";
bool SLEEP_SETTING = false;

int main(int argc, char *argv[]) {
#ifdef test_mode
    test();
//#else
//    JSON().check_json_correctness();
    if(argc > 1 ){
        choose_option(argc, argv);
    }
    system("./get_links.sh"); // for now it is default

//    system("obs-studio --startrecording");
    return 0;
#endif //test_mode

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

