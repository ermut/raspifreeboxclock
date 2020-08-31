#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
An analog clockface with date & time.

Ported from:
https://gist.github.com/TheRayTracer/dd12c498e3ecb9b8b47f#file-clock-py
"""

import math
import time
import datetime
from demo_opts import get_device
from luma.core.render import canvas

import os.path
from luma.core.virtual import viewport
from PIL import Image
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106


def main():
    today_last_time = "Unknown"
    today_last_second = "Unknown"
    images_droite = [
         "ZERO.png",
         "UN droite.png",
         "DEUX.png", 
         "TROIS.png",
         "QUATRE.png",   
         "CINQ.png",  
         "SIX.png", 
         "SEPT.png", 
         "HUIT.png", 
         "NEUF.png",    
         "NOIR.png"         
    ]
    
    images_gauche = [
         "ZERO.png",
         "UN gauche.png",
         "DEUX.png", 
         "TROIS.png",
         "QUATRE.png",   
         "CINQ.png",  
         "SIX.png", 
         "SEPT.png", 
         "HUIT.png", 
         "NEUF.png",    
         "NOIR.png"         
    ]
    
    images_droite_ = [
         "ZERO_.png",
         "UN droite_.png",
         "DEUX_.png", 
         "TROIS_.png",
         "QUATRE_.png",   
         "CINQ_.png",  
         "SIX_.png", 
         "SEPT_.png", 
         "HUIT_.png", 
         "NEUF_.png",    
         "NOIR_.png"         
    ]
    
    images_gauche_ = [
         "ZERO_.png",
         "UN gauche_.png",
         "DEUX_.png", 
         "TROIS_.png",
         "QUATRE_.png",   
         "CINQ_.png",  
         "SIX_.png", 
         "SEPT_.png", 
         "HUIT_.png", 
         "NEUF_.png",    
         "NOIR_.png"         
    ]
    
    virtual = viewport(device, width=device.width, height=device.height)

    
    while True:
        now = datetime.datetime.now()
        #today_date = now.strftime("%d %b %y")
        #today_time = now.strftime("%H:%M:%S")
        today_second = now.strftime("%S")

        if today_second != today_last_second:
        #if today_time != today_last_time:
            #today_last_time = today_time
            today_last_second = today_second
            #now = datetime.datetime.now()
            today_time = now.strftime("%H:%M:%S")
            today_date = now.strftime("%d %b %y")  
            
            #device.contrast((now.second % 2)*255)
            

            with canvas(virtual) as draw:
                    #SECONDES
                    #secondes  dizaine
                    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'freefont', images_gauche_[now.second // 10]))
                    chiffre = Image.open(img_path)
                    draw.bitmap((37, 50), chiffre, fill="white")

                    #secondes  unité
                    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'freefont', images_droite_[now.second % 10]))
                    chiffre = Image.open(img_path)
                    draw.bitmap((43, 50), chiffre, fill="white")
                    
                    #MINUTES
                    #minutes  unité
                    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'freefont', images_droite[now.minute % 10]))
                    chiffre = Image.open(img_path)
                    # if now.second == 54  :
                     #   draw.bitmap((25 + now.microsecond*22/1000000, 25), chiffre, fill="white")
                    # draw.bitmap((25, 25), chiffre, fill="white")
                    #draw.bitmap((25 + ((now.second % 5)*1000000 + now.microsecond)*22/5000000, 25), chiffre, fill="white")
                    draw.bitmap((25, 25), chiffre, fill="white")
                  

                    #minutes  dizaine
                    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'freefont', images_gauche[now.minute // 10]))
                    chiffre = Image.open(img_path)
                    draw.bitmap((0, 25), chiffre, fill="white")
                        
 
                    #HEURE
                    #heure dizaine
                    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'freefont', images_gauche[now.hour // 10]))
                    chiffre = Image.open(img_path)
                    draw.bitmap((0, 0), chiffre, fill="white")
                        
                    #heure unite
                    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'freefont', images_droite[now.hour % 10]))
                    chiffre = Image.open(img_path)
                    draw.bitmap((25, 0), chiffre, fill="white")
                        
                         
                    #JOURS
                    #jour  dizaine
                    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'freefont', images_gauche_[now.day // 10]))
                    chiffre = Image.open(img_path)
                    draw.bitmap((0, 59), chiffre, fill="white")
                        
                    #jour  unité
                    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'freefont', images_droite_[now.day % 10]))
                    chiffre = Image.open(img_path)
                    draw.bitmap((6, 59), chiffre, fill="white")
 
                    #JOURS
                    #mois  dizaine
                    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'freefont', images_gauche_[now.month // 10]))
                    chiffre = Image.open(img_path)
                    draw.bitmap((15, 59), chiffre, fill="white")
                        
                    #mois  unité
                    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'freefont', images_droite_[now.month % 10]))
                    chiffre = Image.open(img_path)
                    draw.bitmap((21, 59), chiffre, fill="white")
 
                    #draw.line((cx, cy, cx + hrs[0], cy + hrs[1]), fill="white")
                    draw.rectangle((12, 62, 13, 63), outline="white")

        #time.sleep(0.1)


if __name__ == "__main__":
    try:
        serial = i2c(port=1, address=0x3C)
        # https://luma-oled.readthedocs.io/en/latest/_modules/luma/oled/device.html
        device = ssd1306(serial, rotate=1, width=64, height=48)
        #device = get_device()
        device.contrast(0)
        main()
    except KeyboardInterrupt:
        pass
