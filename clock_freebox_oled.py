# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# Imports the necessary libraries...
# ERMUT : this program is designed to run an adafruit OLED 128x64 device

import time
import board
#import digitalio
import datetime

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import os.path


#def main():
today_last_time = -1
today_last_second = -1
today_last_minute = -1
today_last_hour = -1
today_last_day = -1
today_last_month = -1
today_last_year = -1
flag_minute = -1

LEFT = True
RIGHT = False


number_right = [
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "ZERO.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "UN droite.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "DEUX.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "TROIS.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "QUATRE.png"))),   
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "CINQ.png"))),  
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "SIX.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "SEPT.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "HUIT.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "NEUF.png")))    
]
number_left = [
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "ZERO.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "UN gauche.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "DEUX.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "TROIS.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "QUATRE.png"))),   
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "CINQ.png"))),  
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "SIX.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "SEPT.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "HUIT.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "NEUF.png")))    
]

number_right_small = [
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "ZERO_.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "UN droite_.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "DEUX_.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "TROIS_.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "QUATRE_.png"))),   
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "CINQ_.png"))),  
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "SIX_.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "SEPT_.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "HUIT_.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "NEUF_.png")))    
]
number_left_small = [
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "ZERO_.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "UN gauche_.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "DEUX_.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "TROIS_.png"))),
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "QUATRE_.png"))),   
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "CINQ_.png"))),  
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "SIX_.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "SEPT_.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "HUIT_.png"))), 
     Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'freeboxfont_', "NEUF_.png")))    
]

# Setting some variables for our reset pin etc.
#RESET_PIN = digitalio.DigitalInOut(board.D4)

i2c = board.I2C()
#oled = adafruit_ssd1306.SSD1306_I2C(64, 48, i2c, addr=0x3C, reset=RESET_PIN)
#oled = adafruit_ssd1306.SSD1306_I2C(64, 64, i2c, addr=0x3C)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
#oled.rotation = 1
oled.contrast = 0

LARGE = number_left[0].width
SMALL = number_left_small[0].width


# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
#image = Image.new("1", (oled.height, oled.width))
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
    

def clear_and_draw (x, y, side, size, index, x_offset, y_offset):
      #Clear the area before drawing 
      draw.rectangle((x, y, x + size -1, y + size -1), outline=0, fill=0)
      if (size == LARGE):
            if (side == LEFT):
            #case we displaying or scrolling large number on the left side of the 4 digits arranged as square   
                  #offset sign is use to undertand the scholling direction
                  if (x_offset > 0) or (y_offset > 0):
                        #if POSITIVE from left to right (x_offset), or top to bottom (y_offset) depending if it is x_offset or y_offset
                        #draw.bitmap((x+x_offset, y+y_offset), number_left[index].crop((0, 0, size-1-x_offset, size-1-y_offset)), fill="white")
                        draw.bitmap((x+x_offset, y+y_offset), number_left[index].crop((0, 0, size-x_offset, size-y_offset)), fill="white")
                  else:
                        #if NEGATIVE from right to left (x_offset), or bottom to top (y_offset) depending if it is x_offset or y_offset
                        #draw.bitmap((x, y), number_left[index].crop((-x_offset, -y_offset, size-1, size-1)), fill="white")
                        draw.bitmap((x, y), number_left[index].crop((-x_offset, -y_offset, size, size)), fill="white")

            #case we displaying or scrolling large number on the right side of the 4 digits arranged as square   

            else:
                  if (x_offset > 0) or (y_offset > 0):
                        #if POSITIVE from left to right (x_offset), or top to bottom (y_offset) depending if it is x_offset or y_offset
                        #draw.bitmap((x+x_offset, y+y_offset), number_right[index].crop((0, 0, size-1-x_offset, size-1-y_offset)), fill="white")
                        draw.bitmap((x+x_offset, y+y_offset), number_right[index].crop((0, 0, size-x_offset, size-y_offset)), fill="white")
                  else:
                        #if NEGATIVE from right to left (x_offset), or bottom to top (y_offset) depending if it is x_offset or y_offset
                        #draw.bitmap((x, y), number_right[index].crop((-x_offset, -y_offset, size-1, size-1)), fill="white")
                        draw.bitmap((x, y), number_right[index].crop((-x_offset, -y_offset, size, size)), fill="white")
      else:
            #for the small digits there is no scrolling capapbilities
            if (side == LEFT):
                  draw.bitmap((x, y), number_left_small[index], fill="white")
            else:
                  draw.bitmap((x, y), number_right_small[index], fill="white")
      oled.image(image)
      oled.show()
      
#Draw small points arround the date
draw.rectangle((101, 10, 103, 12), outline=1, fill=1)
draw.rectangle((115, 24, 117, 26), outline=1, fill=1)

            
while True:
    
      now = datetime.datetime.now()
      today_second = now.second
      today_minute = now.minute
      today_hour = now.hour
      today_day = now.day
      today_month = now.month
      today_year = now.year

      if (today_second != today_last_second) or (today_second == 59) or (today_second == 0):
 
            if (today_second != today_last_second):
                  today_last_second = today_second
                  #secondes  dizaine
                  clear_and_draw(66, 51, LEFT, SMALL, today_second // 10, 0, 0)
                  #secondes  unité
                  clear_and_draw(80, 51, RIGHT, SMALL, today_second % 10, 0, 0)
            
            #Wait to reach the exact beginig of second 59
            if (today_second == 58):
                  while (datetime.datetime.now().second == 58):
                        time.sleep(0.01)
            
            if (today_minute != today_last_minute) or (today_second == 59) or (today_second == 0):
                  
                  offset = LARGE * now.microsecond / 1000000
                  #remove number to the horizontal direction
                  if (today_second == 59):
                        #offset = LARGE * now.microsecond / 1000000
                        clear_and_draw(33, 34, RIGHT, LARGE, today_minute % 10, offset, 0)

                        #tenth of second is also changing
                        if (today_minute % 10 == 9):
                              clear_and_draw(0, 34, LEFT, LARGE, today_minute // 10, -offset, 0)
                  else:
                        #introduce number from the vertical direction
                        if (today_second == 0):
                              #offset = LARGE - LARGE * now.microsecond / 1000000
                              clear_and_draw(33, 34, RIGHT, LARGE, today_minute % 10, 0, LARGE - offset)
                              #tenth of second is also changing
                              if (today_minute % 10 == 0):
                                    clear_and_draw(0, 34, LEFT, LARGE, today_minute // 10, 0, LARGE - offset)
                        else:
                              #ALL OTHER TYPE OF MINUTES and from case (today_minute != today_last_minute) to set full position (no scroll) after 0 seconds
                              today_last_minute = today_minute
                              #minutes  dizaine
                              clear_and_draw(0, 34, LEFT, LARGE, today_minute // 10, 0, 0)
                              #minutes  unité
                              clear_and_draw(33, 34, RIGHT, LARGE, today_minute % 10, 0, 0)

                  if (today_last_hour != today_hour) or (today_second == 59) or (today_second == 0):
                        #remove number to the horizontal direction
                        if (today_minute == 59) and (today_second == 59):
                              #offset = LARGE * now.microsecond / 1000000
                              clear_and_draw(33, 0, RIGHT, LARGE, today_hour % 10, offset, 0)
                              #tenth of hours is also changing
                              if (today_hour % 10 == 9):
                                    clear_and_draw(0, 0, LEFT, LARGE, today_hour // 10, -offset, 0)
                        else:
                              #introduce number from the vertical direction
                              if (today_minute == 0) and (today_second == 0):
                                    #offset = LARGE - LARGE * now.microsecond / 1000000
                                    #clear_and_draw(33, 0, RIGHT, LARGE, today_hour % 10, 0, -offset)
                                    clear_and_draw(33, 0, RIGHT, LARGE, today_hour % 10, 0, -(LARGE - offset))
                                    #tenth of hours is also changing
                                    if (today_hour % 10 == 0):
                                          #clear_and_draw(0, 0, LEFT, LARGE, today_hour // 10, 0, -offset)
                                          clear_and_draw(0, 0, LEFT, LARGE, today_hour // 10, 0, -(LARGE - offset))
                              else: 
                                    #ALL OTHER TYPE OF HOURS and from case (today_last_hour != today_hour) to set full position  (no scroll) after 0 seconds 
                                    today_last_hour = today_hour
                                    #heure dizaine
                                    clear_and_draw(0, 0, LEFT, LARGE, today_hour // 10, 0, 0)
                                    #heure unite
                                    clear_and_draw(33,0, RIGHT, LARGE, today_hour % 10, 0, 0)
                                    
                        
                        if (today_last_day != today_day):
                              today_last_day = today_day
                              #jour  dizaine
                              clear_and_draw(73, 0, LEFT, SMALL, today_day // 10, 0, 0)
                              #jour  unité
                              clear_and_draw(87, 0, RIGHT, SMALL, today_day % 10, 0, 0)

                              if (today_last_month != today_month):
                                    today_last_month = today_month
             
                                    #mois  dizaine
                                    clear_and_draw(87, 15, LEFT, SMALL, today_month // 10, 0, 0)
                                    #mois  unité
                                    clear_and_draw(101, 15, RIGHT, SMALL, today_month % 10, 0, 0)
                        
                                    if (today_last_year != today_year):
                                          today_last_year = today_year
                               
                                          #annee millier
                                          clear_and_draw(73, 30, LEFT, SMALL, today_year // 1000, 0, 0)
                                          #annee centaine
                                          clear_and_draw(87, 30, LEFT, SMALL, (today_year // 100) % 10, 0, 0)
                                          #annee dizaine
                                          clear_and_draw(101, 30, LEFT, SMALL, (today_year // 10) % 10, 0, 0)
                                          #annee unité
                                          clear_and_draw(115, 30, LEFT, SMALL, today_year % 10, 0, 0)
                              
      #for all cases which do not manage scrolling we wait in order to do not use all the CPU
      if not((today_second == 59) or (today_second == 0)):
            time.sleep(0.3)
