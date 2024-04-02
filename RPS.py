#winning dynamics here 1= rock 2= paper 3=scissor 
def winorlose(x,y):
	if x==y:
		return 0
	elif x==1:
		if y==2:
			return 2
		elif y==3:
			return 1
	elif x==2:
		if y==3:
			return 2
		elif y==1:
			return 1
	elif x==3:
		if y==1:
			return 2
		elif y==2:
			return 1

import pygame
import random
pygame.mixer.init()
soundr= pygame.mixer.Sound('rock.wav')
soundp= pygame.mixer.Sound("paper.wav")
sounds= pygame.mixer.Sound("scissor.wav")


history=[]
with open('history.txt', "r") as f:
  for line in f:
    history.append(line.strip())

#pictures loading 	      
r = pygame.image.load('rock.png')
p= pygame.image.load('paper.png')
s=pygame.image.load('sissor.png')
c=pygame.image.load('click.png')

#just house warming stuff
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
wincount=0
losecount=0
gameDisplay=pygame.display.set_mode((800,800))
pygame.display.set_caption('Rock paper sissor')
pin=1
gameExit=False
textsurface = myfont.render('Rock(left) paper(down) sissor(right) choose one option  ', False, (0, 0, 0))
draw = myfont.render('DRAW  ', False, (0,0, 255))
win = myfont.render('YOU WIN  ', False, (0, 255, 0))
wc = myfont.render(str(wincount), False, (0, 0, 0))
lose = myfont.render('YOU LOSE  ', False, (255, 0, 0))
lc = myfont.render(str(losecount), False, (0, 0, 0))
gameDisplay.fill(white)
gameDisplay.blit(textsurface,(0,0))
pygame.display.update()



#gaem mechanics 
while not gameExit:
    textsurface = myfont.render('Some Text', False, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('history.txt', "w") as f:
                 for s in history:
                     f.write(str(s) +"\n")
            gameExit=True
        if event.type==pygame.KEYDOWN:
             keys=pygame.key.get_pressed()
             
             choice = r
             if event.key == pygame.K_LEFT:
                 pin=1
                 choice = r
                 
             if event.key == pygame.K_DOWN:
                 pin=2
                 choice = p
                 #soundp.play()
             if event.key == pygame.K_RIGHT:
                 pin=3
                 choice = s
                 #sounds.play()
             cin=random.randint(1,3)
             if cin==1:
                 cchoice =r
                 soundr.play()
             if cin==2:
                 cchoice = p
                 soundp.play()
             if cin==3:
                 cchoice = s
                 sounds.play()
             
            
             if winorlose(pin,cin)==1:
                gameDisplay.fill(white)
                gameDisplay.blit(win,(350,250))
                wincount+=1
                gameDisplay.fill(white)
             elif winorlose(pin,cin)==2:
                 gameDisplay.fill(red)
                 gameDisplay.blit(lose,(350,250))
                 losecount+=1
                 
             else:
                 gameDisplay.blit(draw,(350,250))
             gameDisplay.blit(choice,(300,300))
             gameDisplay.blit(cchoice,(300,40))
             wc = myfont.render('wins-'+str(wincount), False, (0, 0, 255))
             lc = myfont.render('loss-'+str(losecount), False, (0, 0, 255))
             gameDisplay.blit(wc,(0,20))
             gameDisplay.blit(lc,(600,20))
             gameDisplay.blit(c,(0,500))
             #savind data 
             history.append(str([pin,cin]))
             pygame.display.update()
                 
    

            
    gameDisplay.fill(white)
    #ygame.draw.rect(gameDisplay,black,[lead_x,lead_y,50,50])
    
