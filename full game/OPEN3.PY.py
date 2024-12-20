import pygame
pygame.init()

win = pygame.display.set_mode((709,401))
pygame.display.set_caption("Naruto vs sasuke")

walkRight = [pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NR2.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NR3.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NR1.png')]
walkLeft = [pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NL2.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NL3.png'),pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\NL1.png')]

bg = pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\bg2.jpeg')
stan = pygame.image.load('C:\\Users\\Admin\\Desktop\\NARUTO PYGAME\\pics\\Nstanding.png')

Clock = pygame.time.Clock()

x= 30
y= 290
width=40
height=60
speed = 5
isjump = False   ## if it is jumping ##

jumpheight = 10

left = False
right = False
walkCount= 0


run = True

def redrawgamewindow():
    global left
    global right
    global walkCount
    win.blit(bg,(0,0))

    if walkCount +1 > 6:
        walkCount = 0

    if left and isjump == False:
       win.blit(walkLeft[walkCount//2],(x,y))
       walkCount +=1
    
    elif right and isjump == False:
       win.blit(walkRight[walkCount//2],(x,y))
       walkCount +=1

    elif right and isjump:
        win.blit(walkRight[2],(x,y))

    elif left and isjump:
        win.blit(walkLeft[2],(x,y))

    elif not(isjump):
        win.blit(stan,(x,y))
    
    pygame.display.update()

while run:

    Clock.tick(25)

    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False

      ########## KEYS #################
    keys = pygame.key.get_pressed()

      ########## LEFT ####################
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left = True
        right = False

      ############### RIGHT ###################
    elif keys[pygame.K_RIGHT] and x < 670 - width - speed:
        x += speed
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

     ############# JUMP ########################
    if isjump == False:
        if keys[pygame.K_SPACE]:
            isjump = True
            left = False
            right = False
            walkCount = 0

    else:
        if jumpheight >= -10:
            neg = 1
            
            if jumpheight < 0:
                neg=-1

            y -= (jumpheight **2)* 0.5 * neg
            jumpheight -=1

        else:     
            isjump=False
            jumpheight = 10



    redrawgamewindow()

pygame.quit()  
