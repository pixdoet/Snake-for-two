# Snake For Two Python Version
# Original code from edureka
# https://www.edureka.co/blog/snake-game-with-pygame/
# Mixed bag of trash from the internet and my brain

#!/usr/bin/python2

# 1/4/2020
# I confessed to my crush
# She friendzoned me
# I'm so damn depressed
# I wrote code until 10 pm
# Here's the code
import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake For Two Beta 1.1(NOT WORMY)')
 
clock = pygame.time.Clock()
 
snake_block_1 = 10
snake_block_2 = 10
snake_speed = 17
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
def snake_1(snake_block_1, snake_list_1):
    for x in snake_list_1:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block_2, snake_block_2])

def snake_2(snake_block_2, snake_list_2):
    for x_2 in snake_list_2:
        pygame.draw.rect(dis, blue, [x_2[0], x_2[1], snake_block_2, snake_block_2])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
    x2 = dis_width / 2
    y2 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
    x2_change = 0
    y2_change = 0
 
    snake_list_1 = []
    length_of_snake_1 = 1
    
    snake_list_2 = []
    length_of_snake_2 = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block_1) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block_2) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                print ("Program terminated by user")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_1
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_1
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_1
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
					y1_change = snake_block_1
					x1_change = 0
		if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					x2_change = 0
					y2_change = -snake_block_2
				elif event.key == pygame.K_s:
					x2_change = 0
					y2_change = snake_block_2
				elif event.key == pygame.K_a:
					x2_change = -snake_block_2
					y2_change = 0
				elif event.key == pygame.K_d:
					x2_change = snake_block_2
					y2_change = 0
					
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        if x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
			game_close = True
        x1 += x1_change
        y1 += y1_change
        x2 += x2_change
        y2 += y2_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block_1, snake_block_2])
        snake_head_1 = []
        snake_head_1.append(x1)
        snake_head_1.append(y1)
        snake_list_1.append(snake_head_1)
        if len(snake_list_1) > length_of_snake_1:
            del snake_list_1[0]
        
        snake_head_2 = []
        snake_head_2.append(x2)
        snake_head_2.append(y2)
        snake_list_2.append(snake_head_2)
        if len(snake_list_2) > length_of_snake_2:
			del snake_list_2[0]
 
        for x in snake_list_1[:-1]:
            if x == snake_head_1:
                game_close = True
         
        for x_2 in snake_list_2[:-1]:
			if x_2 == snake_head_2:
				game_close = True
 
        snake_1(snake_block_1, snake_list_1)
        snake_2(snake_block_2, snake_list_2)
 
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block_1) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block_1) / 10.0) * 10.0
            length_of_snake_1 += 1

	if x2 == foodx and y2 == foody:
			foodx = round(random.randrange(0, dis_width - snake_block_2) /10.0) * 10.0
			foody = round(random.randrange(0, dis_height - snake_block_2) /10.0) *10.0
			length_of_snake_2 += 1
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
