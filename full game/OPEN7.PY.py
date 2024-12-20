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
        self.standing = True
        self.hitbox = (self.x +10,self.y +5,80,80)



    def draw(self,win):
        if self.walkCount +1 > 6:
           self.walkCount = 0

        if not(self.standing):

           if self.left:
              win.blit(walkLeft[self.walkCount//2],(self.x,self.y))
              self.walkCount +=1
       
           elif self.right:
               win.blit(walkRight[self.walkCount//2],(self.x,self.y))
               self.walkCount +=1

        else:
            if self.right:
                win.blit(pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NR1.png'),(self.x,self.y))
            else:
                win.blit(pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NL1.png'),(self.x,self.y))

        self.hitbox = (self.x +10,self.y +5,80,80)
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)



class weapons():
    def __init__(self,x,y,width,height,facing):
         self.x = x
         self.y = y
         self.width = width
         self.height = height
         self.facing = facing
         self.vel = 8 * facing 
         self.hitbox = (self.x,self.y,40,40)
    
    def draw(self,win):
        win.blit(pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\shur.png'),(self.x,self.y))
        self.hitbox = (self.x,self.y,40,40)
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)


class enemy():
    walkRightS = [pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\SR2.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\SR3.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\SR1.png')]
    walkLeftS = [pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\SL2.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\SL3.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\SL1.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x,self.end]
        self.speed = 8
        self.walkCount = 0
        self.hitbox = (self.x +10 ,self.y +5,80,80)

    def draw(self,win):
        self.move()

        if self.walkCount +1 > 6:
            self.walkCount = 0

        if self.speed >0:
            win.blit(self.walkRightS[self.walkCount//2],(self.x,self.y))
            self.walkCount += 1

        else:
            win.blit(self.walkLeftS[self.walkCount//2],(self.x,self.y))
            self.walkCount +=  1

        self.hitbox = (self.x +10 ,self.y +5,80,80)
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)


    def move(self):
        if self.speed >0:

            if self.x + self.speed < self.path[1]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walkCount = 0

        else:
            if self.x - self.speed > self.path[0]:
               self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walkCount = 0

    def hit(self):
        print("Hit")
    
run = True

def redrawgamewindow():
    
    win.blit(bg,(0,0))
    naruto.draw(win)
    sasuke.draw(win)
    for shuriken in shurikens:
        shuriken.draw(win)


    pygame.display.update()



naruto = player(500,400,100,100)
sasuke = enemy(30,400,100,100,600)
shurikens = []
throwspeed = 0

while run:
     ############ FRAME RATE #########
    Clock.tick(25)
       #################
    if throwspeed >0:
        throwspeed += 1

    if throwspeed >3:
        throwspeed = 0
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False

    for shuriken in shurikens: 
        
        if shuriken.hitbox[1] + round(shuriken.hitbox[3]/2) > sasuke.hitbox[1] and shuriken.hitbox[1] + round(shuriken.hitbox[3]/2) < sasuke.hitbox[1] + sasuke.hitbox[3]:
            if shuriken.hitbox[0] + shuriken.hitbox[2] > sasuke.hitbox[0] and shuriken.hitbox[0] + shuriken.hitbox[2] < sasuke.hitbox[0] +sasuke.hitbox[2]:
                sasuke.hit()
                shurikens.pop(shurikens.index(shuriken))



        if shuriken.x <699 and shuriken.x>0:
            shuriken.x += shuriken.vel

        else:
            shurikens.pop(shurikens.index(shuriken))

      ########## KEYS #################
    keys = pygame.key.get_pressed()

      ########## SHOOTING #############
    if keys[pygame.K_SPACE] and throwspeed == 0:

        if naruto.left == True:
            facing = -1
        else:
            facing = 1
        
        if len(shurikens) <5:

            shurikens.append(weapons(round(naruto.x + naruto.width//2),round(naruto.y + naruto.height//2),40,40,facing))
            throwspeed = 1
      ########## LEFT ####################
    if keys[pygame.K_LEFT] and naruto.x > naruto.speed:
        naruto.x -= naruto.speed
        naruto.left = True
        naruto.right = False
        naruto.standing = False

      ############### RIGHT ###################
    elif keys[pygame.K_RIGHT] and naruto.x < 690 - naruto.width - naruto.speed:
        naruto.x += naruto.speed
        naruto.left = False
        naruto.right = True
        naruto.standing = False

    else:
        naruto.standing = True
        naruto.walkCount = 0

     ############# JUMP ########################
    if naruto.isjump == False:
        if keys[pygame.K_UP]:
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
