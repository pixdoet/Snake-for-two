#!/usr/bin/python2

import pygame
import os

pygame.init()

width = 800
height = 700

mao_x = 0
mao_y = 0

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Mao is back!!!")

mao = ('oh_crap.jpeg')
cody = ('more_crap.jpeg')
clock = pygame.time.Clock()

class Mao(object):
    def __init__(self):
        self.image = pygame.image.load(mao)
        # mao pos
        self.x = 0
        self.y = 0

    def key_handler(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_LEFT]:
            self.x -= dist
        elif key[pygame.K_RIGHT]:
            self.x += dist

    def draw(self, surface):
        # blit mao at his pos
        surface.blit(self.image, (self.x, self.y))

class Cody(object):
    def __init__(self):
        self.image = pygame.image.load(cody)
        #cody pos
        self.x = 0
        self.y = 0

    def codys_handler(self):
        dist = 5
        cody_key = pygame.key.get_pressed()
        if cody_key[pygame.K_w]:
            self.y -= dist
        elif cody_key[pygame.K_s]:
            self.y += dist
        if cody_key[pygame.K_a]:
            self.x -= dist
        elif cody_key[pygame.K_d]:
            self.x += dist

    def draw(self,surface):
        # blit cody at his pos
        surface.blit(self.image, (self.x, self.y))

mao = Mao()
cody = Cody()
running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.K_q:
        running = False

    mao.key_handler()
    cody.codys_handler()

    if cody.x == mao.x and cody.y == mao.y:
        print ("Collision")
    else:
        print ("ok")

    if cody.y == 800 or cody.y == -800 or cody.x == 700 or cody.x == -700:
        running = False
    
    if mao.y == 800 or mao.y == -800 or mao.x == 700 or mao.x == -700:
        running = False

    screen.fill((255,255,255))
    mao.draw(screen)
    cody.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
