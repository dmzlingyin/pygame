# '''
# shump game
# '''

# import pygame
# from pygame.locals import *
# import random
# import os

# #声音模块的初始化，如果失败，进行提示
# if not pygame.mixer:
# 	print('Sorry!mixer is disabled')


# main_dir = os.path.split(os.path.abspath(__file__))[0]
# data_dir = os.path.join(main_dir, 'data')

# #设置窗口的大小
# WIDTH = 460
# HEIGHT = 320  
# SIZE = (WIDTH,HEIGHT)
# #设置一些基本的颜色
# BLACK = (0,0,0)
# WHITE = (255,255,255)
# RED = (255,0,0)
# GREEN = (0,255,0)
# BLUE = (0,0,255)

# #设置帧的频率
# clock = pygame.time.Clock()
# FPS = 20

# #创建窗口
# screen = pygame.display.set_mode(SIZE)
# pygame.display.set_caption("Snake")

# #Snake类
# class Snake(pygame.sprite.Sprite):
# 	def __init__(self,x,y):
# 		pygame.sprite.Sprite.__init__(self)
# 		self.image = pygame.Surface([20,20])
# 		self.image.fill(GREEN)
# 		self.rect = self.image.get_rect()
# 		self.speed = 10
# 		self.rect.x = x
# 		self.rect.y = y
# 	def MoveRight(self):
# 		self.rect.x += self.speed
# 	def MoveLeft(self):
# 		self.rect.x -= self.speed
# 	def MoveUp(self):
# 		self.rect.y -= self.speed
# 	def MoveDown(self):
# 		self.rect.y += self.speed

# class Food(pygame.sprite.Sprite):
# 	def __init__(self,x,y):
# 		pygame.sprite.Sprite.__init__(self)
# 		self.image = pygame.Surface([20,20])
# 		self.image.fill(WHITE)
# 		self.rect = self.image.get_rect()
# 		self.rect.x = x
# 		self.rect.y = y
# snake_Group = pygame.sprite.Group()
# food_Group = pygame.sprite.Group()
# snake = Snake(random.randrange(10,WIDTH),random.randrange(10,HEIGHT))
# snake_Group.add(snake)
# food = Food(random.randrange(10,WIDTH),random.randrange(10,HEIGHT))
# food_Group.add(food)

# #主函数
# def main():


	

# 	#循环标志位
# 	running = True
# 	while running:
# 		clock.tick(FPS)

# 		#事件处理
# 		for event in pygame.event.get():
# 			if event.type == QUIT:
# 				running = False
# 			elif event.type == KEYDOWN and event.key == K_ESCAPE:
# 				running = False
# 			elif event.type == KEYDOWN and event.key == K_RIGHT:
# 				snake.MoveRight()
# 			elif event.type == KEYDOWN  and event.key == K_LEFT:
# 				snake.MoveLeft()
# 			elif event.type == KEYDOWN and event.key == K_UP:
# 				snake.MoveUp()
# 			elif event.type == KEYDOWN and event.key == K_DOWN:
# 				snake.MoveDown()


# 		#判断bullet是否与mob相撞
# 		# hits = pygame.sprite.groupcollide(bullets,mobs,True,True)
		
# 			hits = pygame.sprite.spritecollide(snake,food_Group,False)
# 			if hits:
# 				print(food_Group[0])
			
# 		#判断player是否与mob相撞
# 		# hits = pygame.sprite.spritecollide(player,mobs,False)
# 		# if hits:
# 		# 	running = False
# 		snake_Group.draw(screen)
# 		food_Group.draw(screen)
		
# 		#更新显示
# 		pygame.display.flip()
# 		screen.fill(BLACK)

		

# 	pygame.quit()


# if __name__ == '__main__':
# 	main()
"""
 Simple snake example.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
 
# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
# Margin between each segment
segment_margin = 3
 
# Set initial speed
x_change = segment_width + segment_margin
y_change = 0
 
 
class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Snake Example')
 
allspriteslist = pygame.sprite.Group()
 
# Create an initial snake
snake_segments = []
for i in range(15):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
 
 
clock = pygame.time.Clock()
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)
 
    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)
 
    # Figure out where new segment will be
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)
 
    # Insert new segment into the list
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)
 
    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)
 
    allspriteslist.draw(screen)
 
    # Flip screen
    pygame.display.flip()
 
    # Pause
    clock.tick(5)
 
pygame.quit()