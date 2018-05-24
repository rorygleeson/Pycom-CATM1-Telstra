
import os
import time
import gc
import urequests as requests
from network import LTE


lte = LTE()

def send_at_cmd_pretty(cmd):
    response = lte.send_at_cmd(cmd).split('\r\n')
    for line in response:
        print(line)

send_at_cmd_pretty('AT+CFUN=0')
send_at_cmd_pretty('AT!="clearscanconfig"')
send_at_cmd_pretty('AT!="addscanfreq band=28 dl-earfcn=9410"') 
send_at_cmd_pretty('AT+CGDCONT=1,"IP","telstra.m2m"') 
send_at_cmd_pretty('AT+CEREG=2') 
send_at_cmd_pretty('AT+CFUN=1')

while not lte.isattached():
    time.sleep(1)
    send_at_cmd_pretty('AT!="showphy"')
    send_at_cmd_pretty('AT!="fsm"')
    send_at_cmd_pretty('AT+CEREG?') 

lte.connect()       # start session
while not lte.isconnected():
    time.sleep(4.0)

print ('connected') 
time.sleep(1.0)

print("now upload to platform......")
r = requests.get("http://myplatform.com/apiendpoint")
print(r)
print(r.text)
# It's mandatory to close response objects as soon as you finished
# working with them. On MicroPython platforms without full-fledged
# OS, not doing so may lead to resource leaks and malfunction.
r.close()

print('disconnect & detach modem')
lte.disconnect()
lte.dettach()

print('clean up')
lte = None
gc.collect()
time.sleep(.2)
print('Done...sleep now for 5 mins')

machine.deepsleep(300000)
