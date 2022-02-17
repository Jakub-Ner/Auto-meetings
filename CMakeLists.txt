cmake_minimum_required(VERSION 3.21)
project(automation_of_studies)

set(CMAKE_CXX_STANDARD 14)

include_directories(./)

add_executable(automation_of_studies
        python_scripts/get_links_from_mails.py
        main.cpp main.h
        get_links.sh
        options.cpp options.h
        variables/test_mode.h
        JSON.cpp JSON.h
        my_time.cpp my_time.h
        )
