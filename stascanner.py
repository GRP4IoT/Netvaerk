import network
station = network.WLAN(network.STA_IF)
station.active(True)
ssid = station.scan()
print('network scan', ssid)

