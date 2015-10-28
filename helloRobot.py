#!/usr/bin/python3
import ctypes
import api
import os
import time
import sys
import struct
import random
from buzzer import Buzzer


def Main():
        command = 1
        buzzer=Buzzer()
        try:
                if api.Initialize():
                        print("Initalized")
                        command = 1
                else:
                        print("Intialization failed")
                
                api.PlayAction(55)
                print('Crawl')
                Run(command)
        except (KeyboardInterrupt):
                api.ServoShutdown()
                sys.exit()
        except():
                api.ServoShutdown()
                sys.exit()

def Run(command):
        while(True):
                if(command == 1):
                        api.PlayAction(52)
                        buzzer.play(4)
                        print('Plank')
                        command = 0
        
                elif(command == 0):
                        api.PlayAction(55)
                        print('Crawl')
                        cry= random.randint(1,4)
                        print(cry)
                        if(cry==3):
                                command = 2
                                print('Cry')
                        else:
                                command=0
                                print('KeepCrawling')
                
                elif(command==2):
                        buzzer.play(1)
                        print('Crying')
        
        
        
        

if __name__ == "__main__": 
  Main()
