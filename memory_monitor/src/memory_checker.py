#!/usr/bin/env python3
# coding: utf-8
"""
This script:

1. Is designed to run continuously & indefinitely.

2. Monitors the overall memory usage (resident set) of the system.

3. If overall memory usage is recorded as >80% for a 15 second (or longer) period,
   the script logs this event along with additional information about the system
   at that time.
   
Author: Walter

Copyright: Copyright 2020, pi-top OS Team Coding Exercise

Credits: Mike Roberts, pi-top OS Team

License: MIT

Version: 1.0.0

Maintainer: Walter

Email: waltermaina@yahoo.com

Status: Production
"""

# Built-in modules
import time
import subprocess
from datetime import datetime
import pathlib

# Third-party modules
import psutil

#Get directory of the executing script
filePath=str(pathlib.Path(__file__).parent.absolute())

class MemoryChecker:
    """
    Monitors RAM usage on a raspberry pi.
    
    Attributes:
    
        time (int): Used to track a 15 seconds duration.
        
        ram_used (int): Percentage of ram currently used.
        
        TIME_MAX (int): Time duration threshold.
        
        RAM_MAX (int): RAM usage threshold.
    """
    
    def __init__(self):
        self.time = 0      # Used to track a 15 seconds duration
        self.ram_used = 0  # Percentage of ram currently used
        self.TIME_MAX = 15 # Time duration threshold
        self.RAM_MAX = 80  # RAM usage threshold
         
    def set_time(self,new_time):
        """
        Sets the time variable to a known figure
        
        Parameters:
        
        new_time (int):  The new value of time
        
        Returns:
        
        none
        
        """
        self.time = new_time
    
    def set_ram_used(self,new_ram_used):
        """
        Sets the ram_used variable to a known figure
        
        Parameters:
        
        new_ram_used (float):  The new % or ram used
        
        Returns:
        
        none 
        """
        self.ram_used = new_ram_used
        
    def get_ram_usage(self):
        """
        Gets the ram usage as a percentage
        
        Parameters:
        
        none
        
        Returns:
        
        float: % of RAM in use
        """
        ram_info = psutil.virtual_memory()
        return ram_info.percent
    
    def get_cpu_usage(self):
        """
        Gets the CPU usage as a percentage
        
        Parameters:
        
        none
        
        Returns:
        
        float: % of CPU in use
        """
        cpu_info = psutil.cpu_times_percent(interval=30.0, percpu=False)
        cpu_usage = "{:.1f}%".format(100.0 - cpu_info.idle)
        return cpu_usage
    
    def log_ram_usage(self):
        """
        Records RAM usage to a file
        
        Parameters:
        
        none
        
        Returns:
        
        none
        """
        # Get total RAM usage
        new_ram_usage = self.get_ram_usage()
        # Get current detailed RAM usage
        byte_ram_usage_results = subprocess.check_output("ps aux", shell=True)
        str_ram_usage_results = byte_ram_usage_results.decode()
        # Get current date and time
        now = datetime.now()
        new_time_incident = now.strftime("%d/%m/%Y %H:%M:%S")
        # Get total CPU usage
        new_cpu_usage = self.get_cpu_usage()
        # Log time when ram threshold was exceeded
        incident_string = str(self.RAM_MAX)+ " % RAM THRESHOLD EXCEEDED AT: "+ new_time_incident + ", TOTAL CPU USAGE: " +new_cpu_usage +", TOTAL RAM USAGE: "+str(new_ram_usage) +"%\n"
        # Add ram usage to log file
        log_file_path = filePath +'/ram_usage_log.txt'
        log_file = open(log_file_path,"a+")
        log_file.write(incident_string)
        log_file.write(str_ram_usage_results)
        log_file.close()
        
    def ram_threshold_exceeded(self):
        """
        Used to check if the 80% RAM used threshold
        has been exceeded for 15 seconds.
        
        Parameters:
        
        none
        
        Returns:
        
        bool: True or False depending on ram use status
        """
        
        if self.time >= self.TIME_MAX and self.ram_used > self.RAM_MAX:
            # Reset time counter
            self.time = 0
            # Dump RAM usage in a file
            self.log_ram_usage()
            return True
        else:
            return False
        
    def run_memory_checker(self):
        """
        Continously checks status of RAM
        
        Parameters:
        
        none
        
        Returns:
        
        none
        """
        try:
            while True:
                # Delay for time monitoring
                time.sleep(1)
                # Get and set RAM status
                ram_status = self.get_ram_usage()
                self.set_ram_used(ram_status)
                # Set time passed after 80% RAM usage was exceeded
                if ram_status > self.RAM_MAX:
                    current_time = self.time + 1
                    self.set_time(current_time)
                else:
                    current_time = 0
                    self.set_time(current_time)
                    
                # Check if RAM usage is over 80% for more than 15s
                status = self.ram_threshold_exceeded()              
        except Exception as e:
            print(str(e))
        

if __name__ == '__main__':
    # Create and run Memory Checker
    mem_monitor = MemoryChecker()
    mem_monitor.run_memory_checker()
