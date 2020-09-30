# Memory Monitor 
## Description
This project creates a Python program that should be run on a Debian-based Linux system, it does the following:
*	Runs continuously & indefinitely
*	Monitors the overall memory usage (resident set) of the system
*	If overall memory usage is recorded as >80% for a 15 second (or longer) period, this event is logged along with additional information about the system at that time. For each incident, the log file will have a line of text followed by a table of values. The line of text will have the time when the incident occurred, the total CPU usage at that time and the total RAM usage at that time. The table will have data on all running processes based on the following column headings:
    * **USER** – the user who owns the process (e.g.  pi).
    * **PID** – process ID of the process (e.g. 2570).
    * **%CPU** – the CPU time used divided by the time the process has been running.
    * **%MEM** – the ratio of the process’s resident set size to the physical memory on the machine.
    * **VSZ** – virtual memory usage of entire process (in KiB).
    * **RSS** – resident set size, the non-swapped physical memory that a task has used (in KiB).
    * **TTY** – controlling tty (terminal).
    * **STAT** – multi-character process state.
    * **START** – starting time or date of the process.
    * **TIME** – cumulative CPU time.
    * **COMMAND** – the command used to start the process (e.g. tail -f /var/log/messages).
    
## Software requirements
1.	For the program to work it requires python3 to have been installed.
2.	The installation script will also install pip3 and the psutil python module. The psutil is a third party python module which was chosen because of its easy to use API when getting the percentage of RAM or CPU in use.

## Source code documents
You can find html documents of the source code in the folder memory_monitor_files/documents.

## Installing the memory monitor service
1.	Make sure your raspberry pi has internet access, because some packages will need to be installed.
2.	Change directory into the memory_monitor_files/memory_monitor/src folder.
3.	Run the install.sh script to install a service for the memory monitor as follows: 
     1. chmod +x install.sh
     2.	sudo ./install.sh, check the output because some authorization to install new packages might be required.
4.	This creates a service named memory_monitor.service that will run on startup. 
5.	Run the command systemctl status memory_monitor.service to check if the service has been started.

## Location of the log file
1.	The log file can be found in the folder memory_monitor_files/memory_monitor/src. 
2.	This path can be changed at line 41 of the file: memory_monitor_files/memory_monitor/src/memory_checker.py.

## Uninstalling the memory monitor service
1.	Run the command sudo systemctl stop memory_monitor.service to stop the service.
2.	Run the command sudo systemctl disable memory_monitor.service to disable the service.
3.	Run the command sudo rm /lib/systemd/system/memory_monitor.service to delete the service unit file.
4.	Run the command sudo systemctl daemon-reload. This will prevent the deleted unit file from being referenced.

## Running the unit tests
For a description of the unit tests done, please view the html documents in the memory_monitor_files/documents folder.
1.	Change directory into the memory_monitor_files/memory_monitor/test folder.
2.	Run the command python3 -m unittest memory_checker_tests.Test 

