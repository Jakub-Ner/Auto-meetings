#ifndef AUTOMATION_OF_STUDIES_MY_TIME_H
#define AUTOMATION_OF_STUDIES_MY_TIME_H

#include <ctime>
const int months[] = {31,
                28,
                31,
                30,
                31,
                30,
                31,
                31,
                30,
                31,
                30,
                31
};
int time_to_wait(const tm &meeting_time);

int how_many_days(int year, int months);

int how_many_leap_years(int year);

bool leap_year(int year);

#endif //AUTOMATION_OF_STUDIES_MY_TIME_H
