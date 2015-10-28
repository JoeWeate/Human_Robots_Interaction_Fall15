import RPi.GPIO as GPIO   #import the GPIO library
import time               #import the time library

class Buzzer(object):
 def __init__(self):
  GPIO.setmode(GPIO.BCM)  
  self.buzzer_pin = 22 #set to GPIO pin 22
  GPIO.setup(self.buzzer_pin, GPIO.IN)
  GPIO.setup(self.buzzer_pin, GPIO.OUT)
  print("buzzer ready")

 def __del__(self):
  class_name = self.__class__.__name__
  print (class_name, "finished")

 def buzz(self,pitch, duration):   #create the function “buzz” and feed it the pitch and duration)
 
  if(pitch==0):
   time.sleep(duration)
   return
  period = 1.0 / pitch     #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
  delay = period / 2     #calcuate the time for half of the wave  
  cycles = int(duration * pitch)   #the number of waves to produce is the duration times the frequency

  for i in range(cycles):    #start a loop from 0 to the variable “cycles” calculated above
   GPIO.output(self.buzzer_pin, True)   #set pin 18 to high
   time.sleep(delay)    #wait with pin 18 high
   GPIO.output(self.buzzer_pin, False)    #set pin 18 to low
   time.sleep(delay)    #wait with pin 18 low

 def play(self, tune):
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(self.buzzer_pin, GPIO.OUT)
  x=0

  print("Playing tune ",tune)
  if(tune==1):
  
   i=0
   for (i=0;i<5;i++)
   {
    self.buzz(1046,0.1);
    time.sleep(0.0);
    self.buzz(987,0.1);
    time.sleep(0.0);
    self.buzz(932,0.1);
    time.sleep(0.0);
    self.buzz(880,0.1);
    time.sleep(0.0);
    self.buzz(830,0.1);
    time.sleep(0.0);
    self.buzz(0,0.5);
    time.sleep(0.5);
   }
   
  elif(tune==2):
   self.buzz(1567,0.05);
   time.sleep(0.0);
   self.buzz(1661,0.05);
   time.sleep(0.0);
   self.buzz(1760,0.05);
   time.sleep(0.0);
   self.buzz(1864,0.05);
   time.sleep(0.0);
   self.buzz(2093,0.05);
   time.sleep(0.0);
   self.buzz(0,0);
   time.sleep(1);
    
    
  elif(tune==3):
   
   j=0
   for (j=0;j<6;j++)
   {
    self.buzz(2093,0.01);
    time.sleep(0.0);
    self.buzz(2349,0.02);
    time.sleep(0.03);
    self.buzz(2093,0.02);
    time.sleep(0.03);
    self.buzz(2349,0.02);
    time.sleep(0.03);
    self.buzz(2093,0.02);
    time.sleep(0.03);
    self.buzz(0,0);
    time.sleep(1);
   }
   
  elif(tune==4):
   self.buzz(261,0.1);
   time.sleep(0.0);
   self.buzz(349,0.1;
   time.sleep(0.0);
   self.buzz(392,0.1);
   time.sleep(0.0)
   self.buzz(0,0);
   time.sleep(1);
   
  elif(tune==5):
    pitches=[1047, 988,523]
    duration=[0.1,0.1,0.2]
    for p in pitches:
      self.buzz(p, duration[x])  #feed the pitch and duration to the func$
      time.sleep(duration[x] *0.5)
      x+=1

  GPIO.setup(self.buzzer_pin, GPIO.IN)

if __name__ == "__main__":
  a = input("Enter Tune number 1-5:")
  buzzer = Buzzer()
  buzzer.play(int(a))
