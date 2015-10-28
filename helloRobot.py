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
                elif(command == 0):
                	
			api.PlayAction(55)
                        print('Crawl')
                        cry= random.randint(1,3)
                        print(cry)
                        if(cry==2):
                                command = 2
                                print('Cry')
                        FB=api.passAccelData(1)
                        print(FB)
                        if( FB > 440 or FB < 350):
          			command = 4
                        
                
                elif(command==2):
                	FB= api.passAccelData(1)
                	print('crying: ')
                	print(FB)
                	buzzer=Buzzer()
                        buzzer.play(1)
              		if( FB > 420 or FB < 360):
          			command = 3
          			
          	elif(command==3):
          		api.PlayAction(52)
          		FB = api.passAccelData(1)
          		buzzer=Buzzer()
          		buzzer.play(2)
          		while(FB > 420 or FB < 360):
          			buzzer=Buzzer()
          			buzzer.play(3)
          			FB = api.passAccelData(1)
          			print(FB)
          		
          		command=1
          		
          	elif(command ==4):
          		buzzer=Buzzer()
          		buzzer.play(1)
          		print('Sorry...')
          		
                        
                        
        
        
        
        

if __name__ == "__main__": 
  Main()
