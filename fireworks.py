import pygame
from mote import Mote
import time
from random import randint

file_rocket = 'rocket.mp3'
file_firecrackers = 'with-firecrackers.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file_rocket)

mote = Mote()
for i in range(1,5):
    mote.configure_channel(i, 16, False)

def twinkle(channel, pixel):
    pygame.mixer.music.play()
    print("Bang!")

    for i in range(0,100):
        r = randint(10, 255)
        g = randint(10, 255)
        b = randint(10, 255)

        mote.set_pixel(channel, pixel, r, g, b)
        mote.show()
        time.sleep(0.005)
    pygame.mixer.fadeout(1)
    time.sleep(1)

def fadeout(channel):
    print("... and fade")
    for level in range(5, 0, -1):
        for pixel in range(0,16):
            mote.set_pixel(channel, pixel, level, level, level)
            mote.show()
        time.sleep(0.005)

mote.clear()

def fire(channel):
    tail_r = randint(0,25)
    tail_g = randint(0,25)
    tail_b = randint(0,25)

    for pixel in range(0, 16):
        mote.set_pixel(channel, pixel, tail_r, tail_g, tail_b)
        mote.show()
        time.sleep(0.05)
        mote.set_pixel(channel, pixel, tail_r-10, tail_g-10, tail_b-10)

    twinkle(channel, pixel)
    fadeout(channel)

try:
    while True:
        for channel in range(1,5):
            fire(channel)

except KeyboardInterrupt:
    mote.clear()

