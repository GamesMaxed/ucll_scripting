#! /usr/bin/env python

import pygame
from datetime import datetime


width, height = 640, 480
screen = pygame.display.set_mode((width, height))
running = 1
last_tick = datetime.now()
x, y = 50, 50
vx, vy = 400, 140

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill((0, 0, 0))

    now = datetime.now()
    delta = now - last_tick
    last_tick = now

    x += vx * delta.total_seconds()
    y += vy * delta.total_seconds()

    if x < 0:
        x = -x
        vx = -vx
    elif x > width:
        x = 2 * width - x
        vx = -vx

    if y < 0:
        y = -y
        vy = -vy
    elif y > height:
        y = 2 * height - y
        vy = -vy
                
        
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 5)
    pygame.display.flip()
