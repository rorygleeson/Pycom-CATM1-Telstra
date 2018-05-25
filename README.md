"# Pycom-CAT-M1-Telstra" 


This code is for the Pycom GPY chip, and uses CAT-M1 on the Telstra network. 
Only one library (urequests.py) is required (in /lib folder). This lib is used for sending http requests. 

The logic is simple.

The device sets up an LTE connection.
It send data to a platform (I.E it does a HTTP post).
It then goes into deep sleep for the set duration.
When duration passed, device wakes up and repeats. 

Code mainly copied from the pycom user forums, so thanks to those guys. 

To do
- build in error handling..
- start testing current consumption and improving battery lifespan (ex disable WIFI, BLE ) 

Performace
- Has worked fine for 3 days, updates every 5 minutes all successfull.
- Sitting on floor, antenna as per diagram. 

==== PREREQUISITE ====

Upgrade GPY to latest firmware using the Pycom Fimrware Updater tool

Also update the radio firmware on the Monarch chip as per here (https://docs.pycom.io/chapter/tutorials/lte/firmware.html)

Modify the APN in the code to suit yours. Best to first test the SIM in a mobile phone, ensure you can get a data connection, then use the same APN in the code. I use telstra.m2m (my SIM is provided by M2MOne/Jasper) 
