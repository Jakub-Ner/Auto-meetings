# Auto-Meetings - DEMO

## Table of Contents
- [Why care](#1)
- [Install](#set-up):
  - [Linux (Ubuntu)](#L)
 - [Disclaimer](#Disclaimer)

<a name="1"> <a/>
## Why care?
Do you find yourself forgetting about next recruitment meeting? Had plans for weekend, but also an interesting webinar? Auto meetings will resolve the problems.
- In the webUI You can see **list of following meetings**. 
- If You want, it can even **check Your mailbox** for new meetings.  
- You can hibernate PC via WebUI, and it will **wake up Your PC** a moment before meeting and **record** the meeting for You.
- If You go on vacation during, e.g. academic year, hibernating PC via WebUI will do to be on all lectures, because Auto-meetings **wakes up the PC at least every 10 hours** to check for new meetings.

Beside that:
- Auto-meetings **runs in the background** as a lightweight systemd service.
- To open WebUI run `auto-meetings` in terminal.
- For installing You must have the ability to open terminal in correct directory and `copy/paste` the commends from [Install section](#set-up).
- It is free.
- It is Open Source so everyone can see what exactly Auto-meetings do on a user mailbox.
- Credentials for mailbox stored in the TOP_SECRET.py can be read/written only by root or auto-meetings user. What means if you have set up root password other than "dupa123", credentials are safe.

-------------------------------------------------
<a name="set-up"> </a> 
<a name="L"> </a> 
## Install for Ubuntu:
1. Install python If You don't have: `sudo apt install python3` <p>
1. Install necessary dependencies: `pip3 install dependencies.txt` <- soon will be added <p>
1. Open `Auto-meetings/scripts/` directory in terminal  <p>
1. Give the installer permission to execute: `sudo chmod +x ./install.sh` <p>
1. Run installer: `sudo ./install.sh` <p>


## Set up for obs-studio

**Tool for finishing recordins**
obs-studio -> Tools -> Output timer -> <p>
- ***Stop recording after*** `1` ***hour `45` minutes*** <p>
- - [x] ***Enable recording timer every time***

#### Set mkv 
*in case program crushing during recording*<p>
obs-studio -> File -> Settings -> Output -> <p>
- ***Recording Format*** `mkv`

#### set Source
- turn off an eye icon next to Screen Capture
- turn on an eye icon next to your meeting app for example Zoom <p>
 *if you do not see Sources go to: *view -> Docks -> Sources*

 ---------------------------------------------------------
 
<a name="Disclaimer"> <a/>
### Disclaimer:

- Internet connection is needed
- PC in hibernated mode uses energy
