'''
shump game
'''

import pygame
from pygame.locals import *
import random
import os

#声音模块的初始化，如果失败，进行提示
if not pygame.mixer:
	print('Sorry!mixer is disabled')


main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

#设置窗口的大小
WIDTH = 650
HEIGHT = 480
SIZE = (WIDTH,HEIGHT)
#设置一些基本的颜色
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#设置帧的频率
clock = pygame.time.Clock()
FPS = 20

#创建窗口
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("shump")

#Player类
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(plane_img,(50,38))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.bottom = HEIGHT - 10
		self.speed = 0
	def update(self):
		self.speed = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed = -10
		if keystate[pygame.K_RIGHT]:
			self.speed = 10

		self.rect.x += self.speed

		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
	def shoot(self):
		bullet = Bullet(player.rect.centerx,player.rect.top)
		all_sprite.add(bullet)
		bullets.add(bullet)
class Mob(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = meteor_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100,-40)
		self.speedy = random.randrange(1,8)
		self.speedx = random.randrange(2,6)
	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100,-40)
			self.speed = random.randrange(1,8)
		if self.rect.left < 0 or self.rect.right > WIDTH:
			self.speedx = -self.speedx
	def boomb(self):
		self.boomb_image = damage_img
		self.boomb_image.set_colorkey(BLACK)
		screen.blit(self.boomb_image,(self.rect.x,self.rect.y))


class Bullet(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = bullet_img
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.bottom += self.speedy
		if self.rect.bottom < 0:
			self.kill()

#加载所有的game Grapics
plane_img = pygame.image.load(os.path.join(data_dir,'enemyBlack2.png')).convert()
bullet_img = pygame.image.load(os.path.join(data_dir,'laserRed07.png')).convert()
meteor_img = pygame.image.load(os.path.join(data_dir,'meteorBrown_med1.png')).convert()
background = pygame.image.load(os.path.join(data_dir,'blue.png')).convert()
background = pygame.transform.scale(background,(650,480))
background_rect = background.get_rect()
damage_img = pygame.image.load(os.path.join(data_dir,'playerShip1_damage2.png')).convert()
#将所有的Player对象集中放在一个list中
all_sprite = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()

all_sprite.add(player)

for i in range(8):
	m = Mob()
	all_sprite.add(m)
	mobs.add(m)


#主函数
def main():


	

	#循环标志位
	running = True
	while running:
		clock.tick(FPS)

		#事件处理
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				running = False
			elif event.type == KEYDOWN and event.key == K_SPACE:
				player.shoot()

		#判断bullet是否与mob相撞
		hits = pygame.sprite.groupcollide(bullets,mobs,True,True)
		

		#销毁几个，就重新生成几个，这样就可以源源不断的产生Mob
		for hit in hits:
			m = Mob()
			all_sprite.add(m)
			mobs.add(m)
			m.boomb()
		#判断player是否与mob相撞
		hits = pygame.sprite.spritecollide(player,mobs,False)
		if hits:
			running = False
			
		all_sprite.update()
		screen.blit(background,(0,0))
		all_sprite.draw(screen)


		#更新显示
		pygame.display.flip()

		

	pygame.quit()


if __name__ == '__main__':
	main()