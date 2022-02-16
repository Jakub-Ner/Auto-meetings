#!/bin/bash
sudo chmod +x get_links.sh
g++ main.cpp options.cpp JSON.cpp -o meetings.exe
echo "done"