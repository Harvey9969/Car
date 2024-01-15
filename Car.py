import pygame
import sys
import random
import time
timer = pygame.time.Clock()
fps = 60
WIDTH, HEIGHT = 1000,1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("car")
cbk1 = pygame.image.load('C:\\Users\\thest\\Downloads\\cbk1.png') #make sure to change the file direction 
cbk1 = pygame.transform.scale(cbk1, (1000, 1000))
cbk11 = pygame.image.load('C:\\Users\\thest\\Downloads\\cbk11.png')
cbk11 = pygame.transform.scale(cbk11, (25, 3000))
cbk12 = pygame.transform.scale(cbk11, (25, 3000))
car1d = pygame.image.load('C:\\Users\\thest\\Downloads\\car1d.png')
car1d = pygame.transform.scale(car1d, (90, 180))
car4u = pygame.image.load('C:\\Users\\thest\\Downloads\\car4u.png')
car4u = pygame.transform.scale(car4u, (80, 180))
car5u = pygame.image.load('C:\\Users\\thest\\Downloads\\car5u.png')
car5u = pygame.transform.scale(car5u, (80, 180))
car3d = pygame.image.load('C:\\Users\\thest\\Downloads\\car3d.png')
car3d = pygame.transform.scale(car3d, (90, 180))
fc = pygame.image.load('C:\\Users\\thest\\Downloads\\fc.png')
fc = pygame.transform.scale(fc, (90, 180))
running = True
fc1 = fc.get_rect()
cbk111 = cbk11.get_rect()
cbk121 = cbk11.get_rect()
car1d1 =  car1d.get_rect()
car3d1 =  car3d.get_rect()
car4u1 = car4u.get_rect()
car5u1 = car5u.get_rect()
cbk2 = cbk1.get_rect()
locationu = [550, 700]
locationd = [250, 400]
fc1.topleft = (650, 500)
car1d1.topleft = (locationd[random.randint(0, 1)], 0)
car3d1.topleft = (locationd[random.randint(0, 1)], 0)
car4u1.topleft = (locationu[random.randint(0, 1)], 0)
car5u1.topleft = (locationu[random.randint(0, 1)], 0)
cbk111.topleft = (650, 0)
cbk121.topleft = (350, 0)
cbk2.topleft = (0, 0)
pygame.init()
font = pygame.font.SysFont('Arial', 30)
a, b, c, d, e, e1, end, end1, done = 0, 1, 1, 0, False, False, 0, 0, False
cars = [car1d1, car3d1, car4u1, car5u1]
while running:
    screen.fill((255, 255, 255)) 
    screen.blit(cbk1,  cbk2)
    if end == 0 and end1 == 0:
        f2l = random.randint(0, 1)
        f2l1 = (f2l+1) % 2
    if a == 0:
        end = 0
        screen.blit(car1d,  car1d1)
        for _ in range(10): 
            car1d1.y += 1
        if car1d1.y == 800:
            car1d1.topleft = (locationd[f2l], 0)
            a, b, car1d1.y, end = f2l, f2l1, 0, 1
    if b == 0:
        end = 0
        screen.blit(car3d,  car3d1) 
        for _ in range(20): 
            car3d1.y += 1
        if car3d1.y == 800:
            car3d1.topleft = (locationd[f2l1], 0)
            a, b, car3d1.y, end = f2l, f2l1, 0, 1
    if end == 1 and (random.randint(0, 2) % 3 == 0 or e):
        car1d1.x = locationd[f2l]
        car3d1.x = locationd[f2l1]
        a, b, e = 1, 1, True
        screen.blit(car1d,  car1d1)
        screen.blit(car3d,  car3d1) 
        for _ in range(5): 
            car1d1.y += 1
        for _ in range(10): 
            car3d1.y += 1
        if car1d1.y == 1000:
            car3d1.topleft = (locationd[f2l1], 0)
            car1d1.y = 0
            car1d1.topleft = (locationd[f2l], 0)
            a, b, end, e = f2l, f2l1, 0, False
    if c == 0:
        end1 = 0
        screen.blit(car4u,  car4u1)
        for _ in range(5): 
            car4u1.y += 1
        if car4u1.y == 800:
            car4u1.topleft = (locationu[f2l], 0)
            c, d, car4u1.y, end1 = f2l, f2l1, 0, 1
    if d == 0:
        end1 = 0
        screen.blit(car5u,  car5u1) 
        for _ in range(10): 
            car5u1.y += 1
        if car5u1.y == 800:
            car5u1.topleft = (locationu[f2l1], 0)
            c, d, car5u1.y, end1 = f2l, f2l1, 0, 1
    if end1 == 1 and (random.randint(0, 2) % 3 == 0 or e1):
        car4u1.x = locationu[f2l]
        car5u1.x = locationu[f2l1]
        c, d, e1 = 1, 1, True
        screen.blit(car4u,  car4u1)
        screen.blit(car5u,  car5u1) 
        for _ in range(5): 
            car4u1.y += 1
        for _ in range(10): 
            car5u1.y += 1
        if car4u1.y == 1000:
            car4u1.topleft = (locationu[f2l1], 0)
            car4u1.y = 0
            car5u1.topleft = (locationu[f2l], 0)
            c, d, end1, e1 = f2l, f2l1, 0, False
    for _ in range(10):
        cbk111.y += 1
        cbk121.y += 1
    if cbk111.y == 20:
        cbk111.y = -100
        cbk121.y = -100
    screen.blit(cbk11,  cbk111)
    screen.blit(cbk12,  cbk121)
    screen.blit(fc,  fc1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and 220 <= fc1.x <= 830:
        fc1.x -= 10
    elif keys[pygame.K_RIGHT] and 220 <= fc1.x <= 830:
        fc1.x += 10
    elif fc1.x < 220 or fc1.x > 830:
        done = True
    #220, 830 and change second if to elif and add else for game over
    #print(car1d1.topleft, car1d1.topright, car1d1.bottomleft, car1d1.bottomright)
    #print(fc1.topleft, fc1.topright, fc1.bottomleft, fc1.bottomright)
    for i in cars:
        if i.bottomleft[0] < fc1.topleft[0] < i.bottomright[0] and i.topright[1] < fc1.topleft[1] < i.bottomright[1]:
            done = True
        if i.bottomleft[0] < fc1.topright[0] < i.bottomright[0] and i.topleft[1] < fc1.topright[1] < i.bottomleft[1]:
            done = True
        if i.topleft[0] < fc1.bottomright[0] < i.topright [0] and i.topleft[1] < fc1.bottomleft[1] < i.bottomleft[1]:
            done = True
        if i.topleft[0] < fc1.bottomleft[0] < i.topright [0] and i.topright[1] < fc1.bottomright[1] < i.bottomleft[1]:
            done = True
    if done:
        pygame.draw.rect(screen, 'black', [300, 200, 400, 70])
        img = font.render('You crash', True, 'white')
        screen.blit(img,  (450, 200))
    pygame.display.flip()
    timer.tick(500)
pygame.quit()