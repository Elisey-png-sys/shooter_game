#Создай собственный Шутер!

from pygame import *
#создай игру "Лабиринт"!
# подключение 
from random import *
import pygame

miss = 0
def game():
    global miss
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("space.ogg")
    pygame.mixer.music.play()



    windown = pygame.display.set_mode((700,500))#создание экрана
    fps = pygame.time.Clock()#создание фпс

    fon = pygame.image.load("galaxy.jpg")
    fon = pygame.transform.scale(fon, (700,500))

    class GameObject(pygame.sprite.Sprite):
        def __init__(self, image, visota, shirina, x,y, speed):
            super().__init__()
            self.img_sprite = pygame.image.load(image)
            self.img_sprite = pygame.transform.scale(self.img_sprite,(visota,shirina))

            self.rect = self.img_sprite.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.move = ""

            self.speed = speed
        def show(self):
            windown.blit(self.img_sprite, self.rect)

    class  GamePlayer(GameObject):
        def ypravlenie(self):
            keys = pygame.key.get_pressed()
            if keys [pygame.K_d] and self.rect.x < 650:
                self.rect.x += self.speed
            if keys[pygame.K_a] and self.rect.x > 0:
                self.rect.x -= self.speed
            if keys[K_UP] and self.rect.y  > 0:
                self.rect.y  -= self.speed
            if keys[K_DOWN] and self.rect.y < 700:
                self.rect.y += self.speed
        def vistrel(self):
            puly = Puly("bullet.png",15,20,self.rect.x,self.rect.y,10)
            pulys.add(puly)
            
    miss = 0

    class Enemi(GameObject):
        def forward(self):
            global miss
            self.rect.y += 2
            if self.rect.y > 400:
                miss += 1
                self.rect.y = -20
                self.rect.x = randint(0,700)
            
   

    class Puly(GameObject):
        def update(self):
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.kill()

    pulys = pygame.sprite.Group()


    run = True






    monsters = pygame.sprite.Group()
    for i in range(5):
        monster = Enemi('ufo.png', 50, 50, randint(0,650), -20, 10)
        monsters.add(monster)


    player = GamePlayer("rocket.png",60, 60, 20, 425, 5)


    score = 0
    miss = 0
    while run:
        windown.blit(fon,(0,0))
        for  i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
                break
            elif i.type == KEYDOWN:
                if i.key == K_SPACE:
                    player.vistrel()

        result = f"Вы уничтожали:  {str(score)}"
        bed = font.Font(None, 35).render(result, True, (255,255,255))

        windown .blit(bed,(50,250))


        result1 = f"Вы пропустили:  {str(miss)}"
        bed1 = font.Font(None, 35).render(result1, True, (255,255,255))

        windown .blit(bed1,(50,10))



        kill = pygame.sprite.groupcollide(pulys, monsters, True, True)
        for i in kill:
            monster = Enemi('ufo.png', 50, 50, randint(0,650), -20, 10)
            monsters.add(monster)
            score+=1

        if miss > 10:
            run =  False

        for i in monsters:
            i.forward()
            i.show()
            if i.rect.colliderect(player.rect ):
                run = False

        for i in pulys:
            i.show()
            i.update()


        player.show()
        player.ypravlenie()
        
        pygame.display.update()
        fps.tick(60)




















