# Auto-Meetings

**What makes it useful:**

- Searches on mailbox for mails with information about meetings.
- Saves links and dates of meetings in JSON.
- Saves links and dates you give as params using --add
- looks for the closest meeting
- joins meeting when it should and if user agreed, starts recording
- runs in the background
- can hibernate till next meeting, then hibernate till...


- ---------------------------------------------
*Soon program will:*

- *Starts itself after PC turn on.*

## Set up for Linux (Ubuntu):

Firstly go to automation-of-studies directory <p>
Give set_up.sh permission: `sudo chmod +x set_up.sh` <p>
Run set_up.sh: `./set_up.sh` <p>
Then You can run the program: `./meetings.exe`

-----------------------------------

## Set up for Windows:

Run set_up.bat: `./set_up.bat` <p>
Then You can run the program: `./meetings.exe`

-----------------------------------

## Set up for obs-studio

### Tool for finishing recordins
obs-studio -> Tools -> Output timer -> <p>
- ***Stop recording after*** `1` ***hour `45` minutes*** <p>
- - [x] ***Enable recording timer every time***

### Set mkv 
*in case program crushing during recording*<p>
obs-studio -> File -> Settings -> Output -> <p>
- ***Recording Format*** `mkv`

## set Source
- turn off an eye icon next to Screen Capture
- turn on an eye icon next to your meeting app for example Zoom <p>
 *if you do not see Sources go to: *view -> Docks -> Sources*
-------------------------------------------------

## Parameters

You can run the program with parameters:

- `-h` or `--help` 
- `-a` or `--add "link" "date"` - where link is the link and date is the date of the meeting
- `-s` or `--sleep` - it is recommended to run with sudo
- `-r` or `--record`

***examples:*** <p>
`./meetings.exe --help`  <p>
`sudo ./meetings.exe -s`

## Disclaimer

- Internet connection is needed
- sudo is needed to hibernate PC
- if you want program to search for mails with meetings, you should have installed `Python3`
- PC in hibernated mode uses energy
- Program is designed for non-IT people, that's why .exe is in the repo. Despite this it is
 recommended to delete this file (new one will be generated after `./set_up.sh`, but you are sure what was compiled) 
