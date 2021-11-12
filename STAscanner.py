import network
station = network.WLAN(network.STA_IF)
station.active(True)
ssid = station.scan()
rssi = 0
for i in ssid:
    if i[0] == b'beacon-1':
        print(i)
        rssi = i[4]
        print(rssi)
