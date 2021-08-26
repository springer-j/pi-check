from gpiozero import CPUTemperature
from time import sleep
import sys
import argparse

#######################################
### argparse object and information ###

parser = argparse.ArgumentParser(description='A tool for monitoring CPU temperature for the Raspberry Pi 4.')
parser.add_argument('-s',"--show_all",help="Prints all readings for evaluating temp changes.",action="store_true")


args = parser.parse_args()

show_all = args.show_all

#######################################

cpu = CPUTemperature()

c_temp = cpu.temperature
f_temp = (c_temp * 1.8) + 32



try:
    while True:
        if show_all:
            print(' > ' + f_temp)
        else:
            print(f_temp,end="\r")
except KeyboardInterrupt:
    sys.exit()

