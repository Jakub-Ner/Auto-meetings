#!/bin/bash
sudo chmod +x get_links.sh
g++ main_functionalities/main.cpp main_functionalities/options.cpp main_functionalities/JSON.cpp main_functionalities/my_time.cpp -pthread -o meetings.exe
echo "completed setting up"