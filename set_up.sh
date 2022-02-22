#!/bin/bash
sudo chmod +x get_links.sh
g++ main_funtionalities/main.cpp main_funtionalities/options.cpp main_funtionalities/JSON.cpp main_funtionalities/my_time.cpp -o meetings.exe
echo "done"