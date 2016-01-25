import pygame
from pygame.locals import *

class game(object):
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.WIDTH=1024   # Initialising screen Width
        self.HEIGHT=680   # Initialising screen height
        self.screen=pygame.display.set_mode((self.WIDTH,self.HEIGHT)) # Initialising the canvas
        self.background = pygame.Surface(self.screen.get_size()) # setting background Surface
        pygame.display.set_caption('INTERNSHALA GAME') # setting caption

    def execute_game(self):
        self.screen.fill((0,0,0))
        # Game Instructions
        Intro="Instructions"
        myfont = pygame.font.SysFont("monospace", 30) # setting Font and Size
        label = myfont.render(Intro,1,(255,255,255),(0,0,0)) # rendering text to be displayed
        self.screen.blit(label, (self.WIDTH/4,self.HEIGHT/4)) # Surface blit
        Intro="UP KEY : Move UP"
        label = myfont.render(Intro,1,(255,255,255),(0,0,0))
        self.screen.blit(label, (self.WIDTH/4,self.HEIGHT/4+50))
        Intro="DOWN KEY : Move DOWN"
        label = myfont.render(Intro,1,(255,255,255),(0,0,0))
        self.screen.blit(label, (self.WIDTH/4,self.HEIGHT/4+100))
        Intro="LEFT KEY : Move LEFT"
        label = myfont.render(Intro,1,(255,255,255),(0,0,0))
        self.screen.blit(label, (self.WIDTH/4,self.HEIGHT/4+150))
        Intro="RIGHT KEY : Move RIGHT"
        label = myfont.render(Intro,1,(255,255,255),(0,0,0))
        self.screen.blit(label, (self.WIDTH/4,self.HEIGHT/4+200))
        Intro="Escape Key : EXIT"
        label = myfont.render(Intro,1,(255,255,255),(0,0,0))
        self.screen.blit(label, (self.WIDTH/4,self.HEIGHT/4+250))
        Intro="PRESS ANY KEY TO CONTINUE ..."
        label = myfont.render(Intro,1,(255,255,255),(0,0,0))
        self.screen.blit(label, (self.WIDTH/4,self.HEIGHT/4+400))
        pygame.display.update() # Updating Canvas
        finish=False
        while finish ==False:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN :
                    finish=True

    def __exit__(self):
        pygame.font.quit()   
        pygame.quit()




class fireball(game):
    def __init__(self):
        game.__init__(self)
        self.execute_game()
        self.screen.fill((0,0,0))

        #Initialising our FireBall Object as obj
         
        self.obj=pygame.sprite.Sprite() # Initialising Sprite
        self.obj.image=pygame.image.load('fireball.png') # loading image from the same folder
        self.obj.rect=self.obj.image.get_rect() # getting object's [left,top,width,height]
        self.obj.rect.topleft=[0,0]  # Initialising TopLeft to (0,0)
        self.screen.blit(self.obj.image,self.obj.rect) # Canvas blit
        pygame.display.update()
        

                    
    def execute(self):
        finish=False
        TILE_SIZE=(self.obj.rect.width)/8
        pygame.key.set_repeat(1,75)  # control how held keys are repeated

        # Game Play Loop 
        while finish!=True:
            for event in pygame.event.get():

                        if event.type==pygame.QUIT:
                            finish=True

                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_UP and self.obj.rect.top-TILE_SIZE>=0:
                                self.obj.rect.top-=TILE_SIZE

                            elif event.key==pygame.K_DOWN and self.obj.rect.bottom+TILE_SIZE<=self.HEIGHT:
                                self.obj.rect.bottom+=TILE_SIZE

                            elif event.key==pygame.K_RIGHT and self.obj.rect.right+TILE_SIZE<=self.WIDTH+20:
                                self.obj.rect.right+=TILE_SIZE

                            elif event.key==pygame.K_LEFT and self.obj.rect.left-TILE_SIZE>=0:
                                self.obj.rect.left-=TILE_SIZE

                            elif event.key==pygame.K_ESCAPE:finish=True

                        # Updating our Canvas with latest object coordinates
                        self.screen.fill((0,0,0))
                        myfont = pygame.font.SysFont("monospace", 15) # setting Font and Size
                        label = myfont.render(str(self.obj.rect.x)+','+str(self.obj.rect.y), 1, (255,255,255),(255,0,0)) # Rendering Text to be displayed
                        

                        # Canvas blit and Canvas Update
                        self.screen.blit(label, (0,0)) 
                        self.screen.blit(self.obj.image,self.obj.rect)
                        pygame.display.update()

        


# DRIVING FUNCTION

if __name__=="__main__":
    
    ball=fireball()     # Creating an object of fireball 
    ball.execute()      # Executing Game
    ball.__exit__()     # Exiting Game
