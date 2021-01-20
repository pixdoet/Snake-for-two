import pygame

pygame.init()
dis = pygame.display.set_mode((1080,700))
pygame.display.set_caption('kd 202101201030')
clock = pygame.time.Clock()

class Book(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.image = pygame.image.load('book.jpg')

	def movement(self):
		key = pygame.key.get_pressed()
		if key[pygame.K_w]:
			self.y -= 5
		elif key[pygame.K_s]:
			self.y += 5
		elif key[pygame.K_a]:
			self.x -= 5
		elif key[pygame.K_d]:
			self.x += 5
	def sidewaysmovement(self):
		key = pygame.key.get_pressed()
		if key[pygame.K_q]:
			self.y -= 5
			self.x -= 5
		elif key[pygame.K_e]:
			self.y -= 5
			self.x += 5
		elif key[pygame.K_z]:
			self.y += 5
			self.x -= 5
		elif key[pygame.K_c]:
			self.y += 5
			self.x += 5

	def draw(self,surface):
		surface.blit(self.image, (self.x, self.y))

class Enemy(object):
	def __init__(self):
		self.x = 192
		self.y = 403
		self.image = pygame.image.load('enemy.jpg')
		self.mybullet = pygame.image.load('bullet.jpg')
		self.isTouchingWall = False
		self.steps = 0

	def iHaveBullet(self):
		

        def tempKeyMovement(self):
                key = pygame.key.get_pressed()
                if key[pygame.K_DOWN]:
                        self.y += 3
                elif key[pygame.K_UP]:
                        self.y -= 3
                elif key[pygame.K_LEFT]:
                        self.x -= 3
                elif key[pygame.K_RIGHT]:
                        self.x += 3

	def draw(self,surface):
		surface.blit(self.image, (self.x,self.y))	
book = Book()
enemy = Enemy()
running = True
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False
		print ('Program terminated by user')
	dis.fill((0,0,0))
	book.movement()
	enemy.checkOverBorder()
	enemy.movement()
	enemy.draw(dis)
	book.draw(dis)
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()
