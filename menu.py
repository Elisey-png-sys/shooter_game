import pygame
import   shooter_game 

back = (125,0,225)
windown = pygame.display.set_mode((700,500))#создание экрана
windown.fill(back)
pygame.font.init()

fps = pygame.time.Clock()#создание фпс

button_rect = pygame.Rect(200, 200, 200, 50)
button_exit = pygame.Rect(200, 270, 200, 50)

bed = pygame.font.Font(None,35).render('Начать игру', True, (225,225,225))
exit_b = pygame.font.Font(None, 35).render('Выход', True, (225,225,225))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                shooter_game.game()
                running = False
                pygame.QUIT()


            elif button_exit.collidepoint(event.pos):
                running = False
                pygame.QUIT()
            

    pygame.draw.rect(windown, (22, 66, 168),button_rect)
    pygame.draw.rect(windown, (22, 66, 168),button_exit)

    windown.blit(bed,(225,210))
    windown.blit(exit_b,(250,280))


    pygame.display.update()
    fps.tick(60)
 
    







