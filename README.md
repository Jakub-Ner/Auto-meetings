# Auto-Meetings

**Now program:**

- Searches on my mailbox for mails from my university profesors.
- Looks for links to Zoom Meetings.
- Saves links and dates of meetings in JSON.
- Saves links and dates you give as params using --add
- 

- ---------------------------------------------
*Soon program will:*

- *Starts itself after PC turn on.*
- *Runs in the background.*
- *Joins meetings, when it should.*

## Set up for Linux (Ubuntu):

Firstly go to automation-of-studies directory <p>
Give set_up.sh permission: `sudo chmod +x set_up.sh` <p>
Run set_up.sh: `./set_up.sh` <p>
Then You can run the program: `./meetings.exe`

## Parameters

You can run the program with parameters:

- `--help`
- `--add "link" "date"` - where link is the link and date is the date of the meeting
- `--sleep`
- `--record`

run `./meetings.exe --help to see more details`