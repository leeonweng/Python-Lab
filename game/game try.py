# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 23:23:48 2018

@author: Home love
"""

import pygame
pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("基本架構")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
screen.blit(background, (0,0))
pygame.display.update()
running = True
while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
pygame.quit()
