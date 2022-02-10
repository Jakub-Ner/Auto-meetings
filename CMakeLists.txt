cmake_minimum_required(VERSION 3.21)
project(automation_of_studies)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(automation_of_studies
        python_scripts/get_links_from_mails.py
        main.cpp
        get_links.sh)
