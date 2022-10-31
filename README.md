# wizut_binary_watch
Binary watch for RPi

Created By  : Karol Zyber
Initial Date: 2022-04-27
Last update: 2022-09-25
version ='1.0.1'


Binary watch - python3 script
Wydzial Informatyki ZUT
Studia podyplomowe z zakresu programowania z elementami systemow wbudowanych

Running instructions:
Binary watch: execute main.py - default set to GMT/UTC timezone
Pass a single command line argument of integer number within scope -12 to 12 to set corresponding timezone
To stop press ctrl+c

Logs: 
2022-09-08: version ='1.0'
tests branch creation 

2022-09-25: version ='1.0.1'
tuple instead of list in main file for groupped GPIOs
docstrings & comments correction
bugfix for safety_check.py - correction for characters from ASCII chart
