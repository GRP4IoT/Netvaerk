import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('beacon-1')
sta_if.isconnected()
sta_if.ifconfig()
print('network config:', sta_if.ifconfig())
