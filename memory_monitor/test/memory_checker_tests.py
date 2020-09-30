#!/usr/bin/env python3
# coding: utf-8
"""
Tests the MemoryChecker class in ../src/memory_checker.py

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
import unittest
import sys
import os.path
from os import path

# Changes to the path
sys.path.append('../src')

# This is the class we want to test. So, we need to import it
#from memory_monitor.src.memory_checker import MemoryChecker # use this with pdoc
from memory_checker import MemoryChecker


class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase.
    """
    mem_monitor = MemoryChecker()
    """ An instance of the MemoryChecker class."""


    def test_0_check_time_and_ram_thresholds(self):
        """
        Test case function to check if 15 seconds time and 80% ram thresholds
        have been exceeded.
        """
        print("Start RAM > 80% and Time >= 15 seconds threshold test\n")
        self.mem_monitor.set_time(15)
        self.mem_monitor.set_ram_used(81)

        # check time and ram thresholds
        threshold_exceeded = self.mem_monitor.ram_threshold_exceeded()
        self.assertTrue(threshold_exceeded)  # Test should pass

    def test_1_check_right_time_and_wrong_ram_thresholds(self):
        """
        Test case function to check if 15 seconds time threshold has been
        exceed but the 80% ram threshold has not been exceeded.
        """
        print("Start RAM <= 80% threshold test\n")
        self.mem_monitor.set_time(15)
        self.mem_monitor.set_ram_used(50)

        # check time and ram thresholds
        threshold_exceeded = self.mem_monitor.ram_threshold_exceeded()
        self.assertFalse(threshold_exceeded)  # Test should pass

    def test_2_check_wrong_time_and_right_ram_thresholds(self):
        """
        Test case function to check if 15 seconds time threshold has not been exceeded and
        80% ram threshold has been exceeded.
        """
        print("Start Time < 15 seconds threshold test\n")
        self.mem_monitor.set_time(10)
        self.mem_monitor.set_ram_used(81)

        # check time and ram thresholds
        threshold_exceeded = self.mem_monitor.ram_threshold_exceeded()
        self.assertFalse(threshold_exceeded)  # Test should pass

    def test_3_check_if_log_file_exists(self):
        """
        Test case function to check if the ram_usage_log.txt file was created
        in test 0 (def test_0_check_time_and_ram_thresholds(self):).
        """
        print("Start log file exists test\n")
        # Check first if ram_usage_log.txt exists
        log_exists = path.exists('../src/ram_usage_log.txt')
        self.assertTrue(log_exists)  # Test should pass



if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
