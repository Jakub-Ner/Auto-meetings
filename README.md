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

## Set up for obs-studio

### Tool for finishing recordins
obs-studio -> Tools -> Output timer -> <p>
- ***Stop recording after*** `2` ***hours*** <p>
- - [x] ***Enable recording timer every time***

### Set mkv 
*in case program crushing during recording*<p>
obs-studio -> File -> Settings -> Output -> <p>
- ***Recording Format*** `mkv`

-------------------------------------------------

## Parameters

You can run the program with parameters:

- `-h` or `--help` 
- `-a` or `--add "link" "date"` - where link is the link and date is the date of the meeting
- `-s` or `--sleep`
- `-r` or `--record`

run `./meetings.exe --help to see more details`