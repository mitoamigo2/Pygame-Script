import pygame
pygame.init()
size =  [600, 600]
gravity = 0

screen = pygame.display.set_mode(size)

Player = pygame.image.load('Image.png')
PlayerX = 300
PlayerY = 200
vel =  1

running = True
while running:

    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    userinput = pygame.key.get_pressed()

    if userinput[pygame.K_LEFT]:
        PlayerX -= vel
    if userinput[pygame.K_RIGHT]:
        PlayerX += vel
    if userinput[pygame.K_UP]:
        PlayerY -= vel
    if userinput[pygame.K_DOWN]:
        PlayerY += vel
    
    screen.blit(Player, (PlayerX, PlayerY))

    pygame.display.update()
