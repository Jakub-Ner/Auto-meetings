icacls get_links.bat /grant :(rx)
g++ main_functionalities\main.cpp main_functionalities\options.cpp main_functionalities\JSON.cpp main_functionalities\my_time.cpp -std=c++11 -pthread -o meetings.exe
echo "completed setting up"