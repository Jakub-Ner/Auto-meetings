#include <iostream>
#include "my_time.h"

int time_to_wait(const tm &meeting_time) {
    std::time_t now_in_sec = time(0); // gives actual epoch time since 1970
    tm *now = localtime(&now_in_sec);

    tm diff{};

    diff.tm_year = meeting_time.tm_year - now->tm_year;
    diff.tm_mon = meeting_time.tm_mon - now->tm_mon;
    diff.tm_mday = meeting_time.tm_mday - now->tm_mday;
    diff.tm_hour = meeting_time.tm_hour - now->tm_hour;
    diff.tm_min = meeting_time.tm_min - now->tm_min;

    // doesn't work if now is 28.02 and the meeting is tomorrow 7 a.m.
    if (diff.tm_mday > 1)
        return 60 * 60 * 24;

    return 60 * (diff.tm_min + 60 * (diff.tm_hour + 24 * (diff.tm_mday)));
}

int how_many_days(int year, int month) {
    int total = 0;

    for (int i = 0; i < month; i++) {
        total += months[i];
    }
    if (month > 2 && leap_year(year)) return total + 1;
    return total;
}


int how_many_leap_years(int year) {
    if (leap_year(year)) return year / 4 + 1;
    return year / 4;
}

bool leap_year(int year) {
    if (year % 4 == 0 && year != 200) return true;
    return false;
}