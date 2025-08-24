from matplotlib import pyplot
import time as tm
import subprocess
from matplotlib import pyplot


i = 0
signal_unit = " dBm"
RSSI = "RSSI"
Noise = "Noise"
time_interval = 0.5

def return_snr():
    wifi_dict = {}

    for line in (subprocess.run(['sudo', '/usr/bin/wdutil','info'], capture_output=True, text=True).stdout).splitlines():
        if line.count(':') == 1:
            iline=line.split(':')
            key = iline[0].strip(' '); value = iline[1].strip(' ')
            if key == RSSI or Noise:
                wifi_dict[key] = str(value)
        else:
            continue 

    RSSI_val = int(wifi_dict[RSSI].replace(signal_unit,""))
    NOISE_val= int(wifi_dict[Noise].replace(signal_unit,""))
    return (RSSI_val-NOISE_val)
    
while True:
    i+=1
    
    pyplot.plot(i,return_snr())
    tm.sleep(time_interval)
    