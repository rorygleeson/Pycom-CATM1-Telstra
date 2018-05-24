"# Pycom-CAT-M1-Telstra" 


This code is for the Pycom GPY chip, and uses CAT-M1 on the Telstra network. The logic is simple.

The device sets up an LTE connection.
It send data to a platform (I.E it does a HTTP post).
It then goes into deep sleep for the set duration.
When duration passed, device wakes up and repeats. 

Code mainly copied from the pycom user forums, so thanks to those guys. 


"You Must do this first"

Upgrade GPY to latest firmware using the Pycom Fimrware Updater tool. 
Note 2:
Also update the radio firmware on the Monarch chip as per here (https://docs.pycom.io/chapter/tutorials/lte/firmware.html)
