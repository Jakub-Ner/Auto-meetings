#!\\bin\\bash
icacls get_links.sh /grant :(rx)
g++ main_functionalities\\main.cpp main_functionalities\\options.cpp main_functionalities\\JSON.cpp main_functionalities\\my_time.cpp -o meetings.exe
echo "done"