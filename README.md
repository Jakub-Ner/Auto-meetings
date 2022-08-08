# Auto-Meetings - DEMO

## Table of Contents
- [What makes it useful](#1)
- [Set up](#set-up):
  - [Linux (Ubuntu)](#L)
 - [Disclaimer](#Disclaimer)

<a name="1"> <a/>
## What makes it useful:
- User can manage Auto-meetings via WebUI (to open, use `auto-meetings` in terminal)
- If setted, it Searches on mailbox for mails with information about meetings.
- It Joins meeting when it should and if user agreed, starts recording
- It Runs in the background as a systemd service
- It Can hibernate till next meeting, then hibernate till...

-------------------------------------------------
<a name="set-up"> </a> 
<a name="L"> </a> 
## Set up for Ubuntu:
1. Install python If You don't have: `sudo apt install python3` <p>
1. Install necessary dependencies: `pip3 install dependencies.txt` <- soon will be added <p>
1. Open **Auto-meetings/scripts/** directory in terminal  <p>
1. Give the installer permission to execute: `sudo chmod +x ./install.sh` <p>
1. Run installer: `./install.sh` <p>


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
### Disclaimer

- Internet connection is needed
- PC in hibernated mode uses energy
