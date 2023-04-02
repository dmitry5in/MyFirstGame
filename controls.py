import pygame
import sys


def get_event(cat):
    for event in pygame.event.get():
        """выход"""
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cat.mright = True
            elif event.key == pygame.K_LEFT:
                cat.mleft = True
            elif event.key == pygame.K_UP:
                cat.mup = True
            elif event.key == pygame.K_DOWN:
                cat.mdown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                cat.mright = False
            elif event.key == pygame.K_LEFT:
                cat.mleft = False
            elif event.key == pygame.K_UP:
                cat.mup = False
            elif event.key == pygame.K_DOWN:
                cat.mdown = False