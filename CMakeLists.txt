cmake_minimum_required(VERSION 3.21)
project(automation_of_studies)

set(CMAKE_CXX_STANDARD 14)

include_directories(./)

add_executable(automation_of_studies
        python_scripts/get_links_from_mails.py
        main_funtionalities/main.cpp main_funtionalities/main.h
        get_links.sh
        main_funtionalities/options.cpp main_funtionalities/options.h
        variables/GLOBAL
        main_funtionalities/JSON.cpp main_funtionalities/JSON.h
        main_funtionalities/my_time.cpp main_funtionalities/my_time.h
        variables/operating_systems/MacOS.h
        variables/operating_systems/Windows.h
        )
