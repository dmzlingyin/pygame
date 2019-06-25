'''
人工降雪v1.0
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

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

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
    

def Snow():

	#定义一个雪花lsit
	snow_list = []

	for i in range(300):
		x = random.randrange(0,SIZE[0])
		y = random.randrange(0,SIZE[1])
		x_speed = random.randint(-1,2)
		y_speed = random.randint(3,8)
		snow_list.append([x,y,x_speed,y_speed])
	return snow_list


def main():


	#初始化
	pygame.init()

	screen = pygame.display.set_mode(SIZE)
	#设置标题
	pygame.display.set_caption('唯美雪景')

	#设置鼠标光标不可见
	pygame.mouse.set_visible(0)

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

			
		for i in range(len(snow)):
			#绘制雪花
			pygame.draw.circle(screen,(255,255,255),snow[i][:2],snow[i][3])

			#移动雪花
			snow[i][0] += snow[i][2]
			snow[i][1] += snow[i][3]

			if snow[i][1] > SIZE[1]:
				snow[i][1] = random.randrange(-50,-10)
				snow[i][0] = random.randrange(0,SIZE[0])
		pygame.display.flip()	
		screen.blit(background, (0, 0))
				


	pygame.quit()



if __name__ == '__main__':
	main()