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
                        buzzer=Buzzer()
                        buzzer.play(4)
                        print('Plank')
                        command = 0
			print('Right Left',api.passAccelData(2))
			print('Forward backword',api.passAccelData(1))
                elif(command == 0):
                        print(api.passAccelData(2))
			api.PlayAction(55)
                        print('Crawl')
                        cry= random.randint(1,3)
                        print(cry)
                        if(cry==2):
                                command = 2
                                print('Cry')
                        else:
                                command=0
                                print('KeepCrawling')
                
                elif(command==2):
                	FB= api.passAccelData(2)
                	buzzer=Buzzer()
                        buzzer.play(1)
                        print('Crying')
          		if( FB > 430 || FB < 390):
          			command = 3
          	elif(command==3):
          		api.PlayAction(52)
          		FB = api.passAccelData(2)
          		while(FB > 430 || FB < 390):
          			FB = api.passAccelData(2)
          		
          		command=1
          		
                        
                        
        
        
        
        

if __name__ == "__main__": 
  Main()
