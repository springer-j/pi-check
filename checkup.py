from gpiozero import CPUTemperature
from time import sleep
import sys
import argparse
from statistics import mean

#######################################
### argparse object and information ###

parser = argparse.ArgumentParser(description='A tool for monitoring CPU temperature for the Raspberry Pi 4.')
parser.add_argument('-s',"--show_all",help="Prints all readings for evaluating temp changes.",action="store_true")
parser.add_argument('-d',"--delay",help="Sets delay between temp update.",type=float,default=5)

args = parser.parse_args()

show_all = args.show_all
delay = args.delay


#######################################


all_temps = []


#######################################

def calculate_temps():
    temp_data = {
        "temp_count":str(len(all_temps)),
        "min_temp":str(min(all_temps)),
        "max_temp":str(max(all_temps)),
        "average_temp":str(mean(all_temps))
        }
    return temp_data

def get_temp():
    cpu = CPUTemperature()
    c_temp = cpu.temperature
    f_temp = (c_temp * 1.8) + 32
    f_str = int(f_temp)
    f_str = str(f_str)
    return f_str

try:
    while True:
        temp = get_temp()
        all_temps.append(int(temp))
        if show_all:
            print(' > ' + temp + '°')
            sleep(delay)
        else:
            print(' > ' + temp + '°',end="\r")
            sleep(delay)
            
except KeyboardInterrupt:
    sleep(.5)
    temp_data = calculate_temps()
    temp_data['average_temp'] = str(temp_data['average_temp'])
    print('')
    print(' [!] Samples: ' + temp_data['temp_count'])
    print(' [!] Minimum: ' + temp_data['min_temp'])
    print(' [!] Maximum: ' + temp_data['max_temp'])
    print(' [!] Average: ' + str(temp_data['average_temp'])[0:5])
    sys.exit()