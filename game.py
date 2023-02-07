import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Pie Game")
icon = pygame.image.load('pie.png')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((36,37,80))
    pygame.display.update()
