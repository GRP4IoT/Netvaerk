import network

ssid = 'beacon-1'


ap = network.WLAN(network.AP_IF)

ap.active(True)
ap.config(essid=ssid)

while ap.active() == False:
    pass

print('beacon1 is on')
print(ap.ifconfig()) 
