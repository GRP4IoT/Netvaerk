import network
from time import sleep
station = network.WLAN(network.STA_IF)
station.active(True)
ssid = station.scan()
rssi = 0
while(True):
    for i in ssid:
        if i[0] == b'beacon-1':
            print(i)
            rssi = i[4]
            print(rssi)


    station.active(True)
    station.connect('LTE-1857', '12345678')
    station.isconnected()
    station.ifconfig()
    print('network config:', station.ifconfig())
    sleep(5)
       
        
    station.disconnect();
    print('i am disconnected bitches')
    sleep(5)

    
    
    
