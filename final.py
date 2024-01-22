#Final EX
#Lea Rachel, Tzahi, Daniel,Adir
#8.6.23

from time import sleep
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd


i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1015(i2c)

# Define the ADC pins
chan = AnalogIn(ads, ADS.P0)
voltage_A = AnalogIn(ads, ADS.P1)
voltage_B = AnalogIn(ads, ADS.P2)

# Convert the ADC reading to voltage (0 - 3.3V range)
#def get_voltage(pin):
#    voltage = (pin.value / 65535) * 3.3
#   return voltage

#chan = AnalogIn(ads, ADS.P0)

#---------------------LCD------------------------
GPIO.setwarnings(False) # Disable warnings
GPIO.setmode(GPIO.BCM) # Use BOARD pin numbering

lcd_rs = digitalio.DigitalInOut(board.D26)  #37
lcd_en = digitalio.DigitalInOut(board.D19)  #35
lcd_d4 = digitalio.DigitalInOut(board.D13)  #33
lcd_d5 = digitalio.DigitalInOut(board.D6)   #31
lcd_d6 = digitalio.DigitalInOut(board.D5)   #29
lcd_d7 = digitalio.DigitalInOut(board.D11)  #23
     
# Modify I have a different sized character LCD
lcd_columns = 20
lcd_rows = 4
 
# Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)
 
# Initialise the lcd 
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,lcd_d7, lcd_columns, lcd_rows)

# wipe LCD screen before we start
lcd.clear()

# ---------------------- MAIN ----------------------------

GPIO.setmode(GPIO.BCM) # Use BOARD pin numbering

while True:
  # error = False #Flag
  #  voltage = get_voltage(pin_REF)
   # voltage_A = get_voltage(pin_A)
   # voltage_B = get_voltage(pin_B)

    #GPIO.output(14, GPIO.LOW) # Turn off
    
    if (float(chan.voltage > 0.2) and (float(chan.voltage < 0.4))):
         lcd.message = "voltage_A + voltage_B  = " + "\n" + str(round(voltage_A.voltage + voltage_B.voltage,2))
         print (lcd.message)
         #print("voltage_A + voltage_B = ", voltage_A.voltage + voltage_B.voltage)
         time.sleep(1)
         
    elif (float(chan.voltage > 0.5) and (float(chan.voltage < 0.7))):
                                    
          if (voltage_A.voltage > voltage_B.voltage):
        #    lcd.message = f"voltage_A - voltage_B = {voltage_A - voltage_B}"
            lcd.message = "voltage_A - voltage_B  = " + "\n" + str(round(voltage_A.voltage - voltage_B.voltage,2))
            print (lcd.message)
            #print("voltage_A - voltage_B = ", voltage_A.voltage - voltage_B.voltage)
           
          else:
            #error = True #Flag
            lcd.message = "ERROR"
            print(lcd.message)
            GPIO.output(14, GPIO.HIGH) # Turn on
            sleep(1) # Sleep for 1 second
            GPIO.output(14, GPIO.LOW) # Turn off
            sleep(1) # Sleep for 1 second
                                         
          
    elif (float(chan.voltage > 0.9) and (float(chan.voltage < 1.2))):
          #lcd.message = f"voltage_A * voltage_B = {voltage_A * voltage_B}"
          lcd.message = "voltage_A * voltage_B  = " + "\n" + str(round(voltage_A.voltage * voltage_B.voltage,2))
          print (lcd.message)
          GPIO.output(14, GPIO.LOW) # Turn off
          #print("voltage_A * voltage_B = ", voltage_A.voltage*voltage_B.voltage)
                            
          time.sleep(1)
          
    elif (float(chan.voltage > 1.3) and (float(chan.voltage < 1.7))):
                                    
          if(voltage_B.voltage == 0):
              #error = True #Flag                  
            lcd.message = "ERROR"
            print(lcd.message)
            GPIO.output(14, GPIO.HIGH) # Turn on
            sleep(1) # Sleep for 1 second
            GPIO.output(14, GPIO.LOW) # Turn off
            sleep(1) # Sleep for 1 second
                                    
          else:
            #lcd.message = f"voltage_A / voltage_B = {voltage_A / voltage_B}"
            lcd.message = "voltage_A / voltage_B  = " + "\n" + str(round(voltage_A.voltage / voltage_B.voltage,2))
            print (lcd.message)
            #print("voltage_A / voltage_B = ", voltage_A.voltage / voltage_B.voltage)                    
            time.sleep(1)


    elif (float(chan.voltage > 1.9) and (float(chan.voltage < 2.2))):
          if (voltage_B.voltage == 0):
         #   error = True #Flag                    
            lcd.message = "ERROR"
            print(lcd.message)
            GPIO.output(14, GPIO.HIGH) # Turn on
            sleep(1) # Sleep for 1 second
            GPIO.output(14, GPIO.LOW) # Turn off
            sleep(1) # Sleep for 1 second
          else:
            #lcd.message = f"voltage_A // voltage_B = {voltage_A // voltage_B}"
            lcd.message = "voltage_A // voltage_B = " + "\n" + str(round(voltage_A.voltage // voltage_B.voltage,2))
            print (lcd.message)
            #print("voltage_A // voltage_B = ", voltage_A.voltage // voltage_B.voltage)                        
            time.sleep(1)

    elif (float(chan.voltage > 2.4) and (float(chan.voltage < 2.6))):
          #lcd.message = f"voltage_A ** voltage_B = {voltage_A ** voltage_B}"
          lcd.message = "voltage_A ** voltage_B = " + "\n" + str(round(voltage_A.voltage ** voltage_B.voltage,2))
          print (lcd.message)
          #print("voltage_A ** voltage_B = ", voltage_A.voltage ** voltage_B.voltage)                         
          time.sleep(1)
            

    elif (float(chan.voltage > 2.7) and (float(chan.voltage < 3.0))):
          if (voltage_B.voltage == 0):
          #   error = True #Flag                      
             lcd.message = "ERROR"
             print(lcd.message)
             GPIO.output(14, GPIO.HIGH) # Turn on
             sleep(1) # Sleep for 1 second
             GPIO.output(14, GPIO.LOW) # Turn off
             sleep(1) # Sleep for 1 second
          else:
            # lcd.message = f"voltage_A % voltage_B = {voltage_A % voltage_B}"
             lcd.message = "voltage_A % voltage_B = " + "\n" + str(round(voltage_A.voltage % voltage_B.voltage,2))
             print (lcd.message)
             #print("voltage_A % voltage_B = ", voltage_A.voltage % voltage_B.voltage)
                                    
             time.sleep(1)

    elif (float(chan.voltage > 3.0) and (float(chan.voltage < 3.3))):
          if (voltage_A.voltage<voltage_B.voltage):
            lcd.message = "voltage B is greater than voltage A"     
          else:
            lcd.message = "voltage A is greater than voltage B"
          print(lcd.message)
          time.sleep(1)
        
    elif ((chan.voltage < 0.2) and (voltage_B.voltage < 0.2) and (voltage_A.voltage < 0.2)):

          lcd.clear()

                                    
