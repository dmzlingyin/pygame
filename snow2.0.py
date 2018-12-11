'''
人工降雪
Data:2018-12-09
Author:Lingyin
reference:https://mp.weixin.qq.com/s/fki-eGBzrSsz2xDbk--vpw


'''

import pygame
import random
import os
from pygame.locals import *
from pygame.compat import geterror

if not pygame.mixer: print('Warning, sound disabled')

SIZE = (1300,700)
#设置一些基本的颜色
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

#初始化
pygame.init()

screen = pygame.display.set_mode(SIZE)
#设置标题
pygame.display.set_caption('唯美雪景')

#设置鼠标光标不可见
pygame.mouse.set_visible(0)

#加载图片，利用os模块，实现跨平台
def load_image(name):
	fullname = os.path.join(data_dir,name)

	try:
		image = pygame.image.load(fullname)
	except pygame.error as e:
		raise e
	image = image.convert()
	return image


def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    print(fullname)
    try:
        pygame.mixer.music.load(fullname)
        pygame.mixer.music.play()
    except pygame.error:
        print('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    
class Snow(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.width = random.randrange(5,15)
		self.image = pygame.transform.scale(load_image('snowflake.png'),(self.width,self.width))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(0,1300)
		self.rect.y = random.randrange(0,700)
		self.speedx = random.randrange(-3,5)
		self.speedy = random.randrange(3,5)
	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.x > SIZE[0] or self.rect.x < 0 or self.rect.y > SIZE[1]:
			self.rect.x = random.randrange(0,1300)
			self.rect.y = 0#random.randrange(0,700)	


flow = pygame.sprite.Group()

for i in range(300):
	s = Snow()
	flow.add(s)

def main():


	

	#加载背景
	background = load_image('Lingyin0.jpg')

	screen.blit(background,(0,0))

	#显示背景
	pygame.display.flip()

	clock = pygame.time.Clock()

	snow = Snow()
	
	load_sound('flower.mp3')

	#主循环
	going = True
	while going:

		clock.tick(20)
		for event in pygame.event.get():
			if event.type == QUIT:
				going = False
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				going = False

			
		flow.update()
		flow.draw(screen)
		
		pygame.display.flip()	
		screen.blit(background, (0, 0))



	pygame.quit()



if __name__ == '__main__':
	main()