#include "my_time.h"
#include <iostream>

int time_to_wait(const tm &meeting_time) {
    std::time_t now_in_sec = time(0); // gives actual epoch time
    return now_in_sec
           - meeting_time.tm_year * 60 * 60 * 24 *
           - meeting_time.tm_mon  * 60 * 60 * 24 *
           - meeting_time.tm_mday * 60 * 60 * 24
           - meeting_time.tm_hour * 60 * 60
           - meeting_time.tm_min  * 60;
}
