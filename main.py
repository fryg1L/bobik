import pygame
from player import dino
from enemies import enemies
from clouds import cloud

pygame.init()
size = 1200, 720
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Динозаврик')

font = pygame.font.Font('sprites/Minecraft Seven_2.ttf', 40)
button_surface = pygame.Surface((400, 100))
button_surface.fill((0, 0, 0))
start_text = font.render("Начать Игру", 0, 'white')

quit_but_surface = pygame.Surface((400, 100))
quit_but_surface.fill((0, 0, 0))
quit_text = font.render("Покинуть игру", 0, "white")

main_surface = pygame.image.load('sprites/background.png')
ground_surface = pygame.image.load('sprites/ground.png')

#start_button = pygame.image.load('sprites/start_button.png')
count = 0
text = font.render(f'Cчёт: {count}', 0, 'blue')

enemies_sprite = pygame.sprite.Group()
enemies = enemies()
enemies_sprite.add(enemies)

player_sprite = pygame.sprite.Group()
player = dino()
player_sprite.add(player)
pygame.display.flip()

decor_sprites = pygame.sprite.Group()
clouds = cloud()
decor_sprites.add(clouds)
pygame.display.flip()

activate = True
running_menu = True
running_game = False
running_end_menu = False


while activate:
    while running_menu:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # этот код реагирует на то, что в области где расположена кнопка старта происходит нажатие
                if 435 < event.pos[0] < 835 and 200 < event.pos[1] < 300:
                    running_menu = False
                    running_game = True
                
                elif 435 < event.pos[0] < 835 and 350 < event.pos[1] < 450:
                    running_game = False
                    running_menu = False
                    activate = False


            if event.type == pygame.QUIT:
                running_game = False
                running_menu = False
                activate = False

        
        screen.blit(main_surface, (0, 0))
        #тут просто кнопка отрисовывается
        screen.blit(button_surface, (435, 200))
        screen.blit(start_text, (480, 215))
        screen.blit(ground_surface, (0, 578))

        screen.blit(quit_but_surface, (435, 350))
        screen.blit(quit_text, (455, 365))


        decor_sprites.draw(screen)
        decor_sprites.update()

        pygame.display.update()

        clock.tick(20)

    count = 0
    player.start_position()
    enemies.start_position()
    enemies.update()

    while running_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
            if event.type == pygame.QUIT:
                running_game = False
                running_menu = False
                activate = False

        if pygame.sprite.collide_mask(player, enemies):
            running_game = False
            running_end_menu = True

        screen.blit(main_surface, (0, 0))
        screen.blit(ground_surface, (0, 578))

        decor_sprites.draw(screen)
        decor_sprites.update()
        enemies_sprite.draw(screen)
        enemies_sprite.update()
        player_sprite.update()
        player_sprite.draw(screen)

        screen.blit(text, (30, 5))
        count += 0.1

        text = font.render(f'Cчёт: {round(count, 1)}', 0, 'blue')
        pygame.display.update()
        clock.tick(45)

    while running_end_menu:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # этот код реагирует на то, что в области где расположена кнопка старта происходит нажатие
                if 435 < event.pos[0] < 835 and 200 < event.pos[1] < 300:
                    running_end_menu = False
                    running_game = True

                elif 435 < event.pos[0] < 835 and 350 < event.pos[1] < 450:
                    running_game = False
                    activate = False
                    running_end_menu = False

            if event.type == pygame.QUIT:
                running_game = False
                running_menu = False
                activate = False
                running_end_menu = False

        font = pygame.font.Font('sprites/Minecraft Seven_2.ttf', 40)
        count_text = font.render(f"Ваш результат: {round(count, 1)}", 0, 'blue')


        screen.blit(main_surface, (0, 0))
        # тут просто кнопка отрисовывается
        screen.blit(button_surface, (435, 200))
        screen.blit(start_text, (480, 215))
        screen.blit(ground_surface, (0, 578))

        screen.blit(quit_but_surface, (435, 350))
        screen.blit(quit_text, (455, 365))
        screen.blit(count_text, (410, 125))

        decor_sprites.draw(screen)
        decor_sprites.update()

        pygame.display.update()

        clock.tick(20)
