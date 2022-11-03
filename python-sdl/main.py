#!/bin/env python

from os import getcwd
from time import sleep
from sdl2 import *
from sys import stderr
import ctypes
import json
import vlc

LOGICAL_WIDTH = 36
LOGICAL_HEIGHT = 28
WIDTH = 36*20
HEIGHT = 28*20

def scc(code):
    if code < 0:
        print(f"ERROR: SDL pooped itself: {SDL_GetError()}", SDL_GetError(), file=stderr)

scc(SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, b"linear"))
scc(SDL_SetHint(SDL_HINT_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR, b"0"))
window = SDL_CreateWindow(b"Bad Apple!!", 0, 0,
                          WIDTH,
                          HEIGHT,
                          SDL_WINDOW_RESIZABLE)
renderer = SDL_CreateRenderer(
               window, -1,
               SDL_RENDERER_PRESENTVSYNC
               | SDL_RENDERER_ACCELERATED)
SDL_RenderSetLogicalSize(renderer, LOGICAL_WIDTH, LOGICAL_HEIGHT)

data = None
with open("../data.json") as f:
    data = json.load(f)

p = vlc.MediaPlayer("file://" + getcwd() + "/../badapple.mp3")
p.play()

running = True
for frame in data:
    if not running:
        break
    for y, row in enumerate(frame):
        for x, col in enumerate(row):
            if col == 1:
                SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)
            else:
                SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255)
            SDL_RenderDrawPoint(renderer, x, y)
    event = SDL_Event()
    while SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == SDL_QUIT:
            running = False
            break
    SDL_RenderPresent(renderer)
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)
    SDL_RenderClear(renderer)
    sleep(1/60)
