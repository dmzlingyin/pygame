'''
此脚本是pygame的模板框架，以后如需编写python游戏，直接引用即可

DATE:2018-12-10
AUTHOR:LINGYIN
GITHUB:github.com/dmzlingyin/
EMAIL:dmzlingyin@163.com
'''

import pygame
from pygame.locals import *

#声音模块的初始化，如果失败，进行提示
if not pygame.mixer:
	print('Sorry!mixer is disabled')

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
FPS = 30




#sparites类
class player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('intro_ball.gif')
		#去除周围的颜色
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.x_speed = 3
		self.y_speed = 5

	def update(self):
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed
		if self.rect.right > WIDTH or self.rect.left < 0:
			self.x_speed = -self.x_speed
		if self.rect.bottom > HEIGHT or self.rect.top < 0:
			self.y_speed = -self.y_speed


#将所有的sprite对象集中放在一个list中
all_sprite = pygame.sprite.Group()

ball = player()

all_sprite.add(ball)

#主函数
def main():


	#创建窗口
	screen = pygame.display.set_mode(SIZE)

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
		
		all_sprite.update()
		all_sprite.draw(screen)


		#更新显示
		pygame.display.flip()

		#擦除Old sprite
		screen.fill(BLACK)

	pygame.quit()


if __name__ == '__main__':
	main()