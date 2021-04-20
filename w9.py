import pygame

pygame.init()
font=pygame.font.Font(None, 20)
height,width=440,640
s=40
pi=3.14
screen = pygame.display.set_mode((width+s+s, height+s+s))
pygame.display.set_caption('sine and cosine')
clock = pygame.time.Clock()
running=True

while running:
    screen.fill((255, 255, 255))
    for even in pygame.event.get():
        if even.type==pygame.QUIT:
            running=False

    pygame.draw.rect(screen, (0, 0, 0), (s,s,width,height), 3)
    pygame.draw.line(screen, (0, 0,0), (width/2+s, s), (width/2+s, height+s),2)
    pygame.draw.line(screen, (0, 0, 0), (s, height/2+s), (width  + s, height/2 + s), 2)
    numy = 1.00
    numx=-3
    for i in range(s+20, height+s, 50):
        text = font.render(str(numy), True, (0,0,0))
        screen.blit(text, (7, i-8))
        numy=numy-0.25
        pygame.draw.line(screen, (0, 0, 0), (s, i), (width+s, i), 1)
    for i in range(s+20, width+s, 100):

        pygame.draw.line(screen, (0, 0, 0), (i, s), (i, height+s), 1)
    for i in range(s + 20, width + s, 50):
        text = font.render(str(numx) + 'п', True, (0, 0, 0))
        screen.blit(text, (i-10, height + s+10))
        numx = numx + 1 / 2
    #GREEN
    for i in range(s+20, width+s-200, 200):
        pygame.draw.arc(screen, (255, 0, 0), (i, 60, 100, height-s), -3.14, 0, 3)
    for i in range(s + 120, width + s - 100, 200):
        pygame.draw.arc(screen, (255, 0, 0), (i, 60, 100, height - 20), 0, 3.14, 3)

    #BLUE
    for i in range(s + 70, width + s - 100, 200):
        pygame.draw.arc(screen, (0, 0, 255), (i, 60, 100, height - 20), 0, 3.14, 3)
    for i in range(s+170, width+s-200, 200):
        pygame.draw.arc(screen, (0, 0, 255), (i, 60, 100, height-s), -3.14, 0, 3)
    #pygame.draw.rect(screen, (255,0,0), (60, 60, 100, height-s), 3)

    pygame.draw.arc(screen, (0, 0, 255), (s-30, 60, 100, height-s), -3.14/2, 0, 3)
    pygame.draw.arc(screen, (0, 0, 255), (s+570, 60, 100, height - s), -3.14, -3.14/2, 3)

    text = font.render('sin x', True, (0, 0, 0))
    screen.blit(text, (450, s+30))
    pygame.draw.line(screen, (255, 0, 0), (490, s+36), (500, s+36), 1)
    text = font.render('cos x', True, (0, 0, 0))
    screen.blit(text, (450, s + 40))
    pygame.draw.line(screen, (0, 0, 255), (490, s + 36+10), (500, s + 36+10), 1)

    numm=-3
    for i in range(s+20, 300,100):
        text = font.render(str(numm), True, (0, 0, 0))
        screen.blit(text, (i, 270))
        numm+=1
    pygame.display.flip()
    clock.tick(60)
pygame.quit()