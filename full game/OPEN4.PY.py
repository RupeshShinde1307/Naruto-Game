import pygame
pygame.init()

win = pygame.display.set_mode((700,500))
pygame.display.set_caption("Naruto vs sasuke")

walkRight = [pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NR2.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NR3.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NR1.png')]
walkLeft = [pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NL2.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NL3.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NL1.png')]

bg = pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\bg.png')
stan = pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\Nstanding.png')

Clock = pygame.time.Clock()

class player():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 10
        self.isjump = False
        self.jumpheight = 10                                                                            
        self.left = False
        self.right = False
        self.walkCount= 0



    def draw(self,win):
        if self.walkCount +1 > 6:
           self.walkCount = 0

        if self.left and self.isjump == False:
           win.blit(walkLeft[self.walkCount//2],(self.x,self.y))
           self.walkCount +=1
    
        elif self.right and self.isjump == False:
           win.blit(walkRight[self.walkCount//2],(self.x,self.y))
           self.walkCount +=1

        elif self.right and self.isjump:
           win.blit(walkRight[2],(self.x,self.y))

        elif self.left and self.isjump:
           win.blit(walkLeft[2],(self.x,self.y))

        elif not(self.isjump):
           win.blit(stan,(self.x,self.y))

run = True

def redrawgamewindow():
    
    win.blit(bg,(0,0))
    naruto.draw(win)
    pygame.display.update()



naruto = player(500,400,100,100)

while run:

    Clock.tick(25)

    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False

      ########## KEYS #################
    keys = pygame.key.get_pressed()

      ########## LEFT ####################
    if keys[pygame.K_LEFT] and naruto.x > naruto.speed:
        naruto.x -= naruto.speed
        naruto.left = True
        naruto.right = False

      ############### RIGHT ###################
    elif keys[pygame.K_RIGHT] and naruto.x < 690 - naruto.width - naruto.speed:
        naruto.x += naruto.speed
        naruto.left = False
        naruto.right = True

    else:
        naruto.left = False
        naruto.right = False
        naruto.walkCount = 0

     ############# JUMP ########################
    if naruto.isjump == False:
        if keys[pygame.K_SPACE]:
            naruto.isjump = True
            naruto.left = False
            naruto.right = False
            naruto.walkCount = 0

    else:
        if naruto.jumpheight >= -10:
            neg = 1
            
            if naruto.jumpheight < 0:
                neg=-1

            naruto.y -= (naruto.jumpheight **2)* 0.5 * neg
            naruto.jumpheight -=1

        else:     
           naruto.isjump=False
           naruto.jumpheight = 10



    redrawgamewindow()

pygame.quit()  
