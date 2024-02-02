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

        f = open('record.txt', 'r')
        data = f.read().split('\n')
        records_text = font.render(f"ТОП 3 РЕКОРДА:", 0, 'blue')
        record1 = font.render(f"{data[0]}", 0, 'blue')
        record2 = font.render(f"{data[1]}", 0, 'blue')
        record3 = font.render(f"{data[2]}", 0, 'blue')
        f.close()

        screen.blit(main_surface, (0, 0))
        screen.blit(button_surface, (435, 200))
        screen.blit(start_text, (480, 215))
        screen.blit(ground_surface, (0, 578))
        screen.blit(records_text, (1, 0))
        screen.blit(record1, (9, 50))
        screen.blit(record2, (9, 100))
        screen.blit(record3, (9, 150))

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
            f = open('record.txt', 'r')
            date = f.read().split('\n')
            data = []
            for x in date:
                if x != '':
                    data.append(float(x.strip()))
            f.close()
            current_record = round(count, 1)
            if current_record > data[2]:
                data.remove(data[2])
                data.append(current_record)
                f = open('record.txt', 'w')
                for x in reversed(sorted(data)):
                    f.write(str(x) + '\n')
                f.close()

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

        count_text = font.render(f"Ваш результат: {round(count, 1)}", 0, 'blue')

        f = open('record.txt', 'r')
        data = f.read().split('\n')
        records_text = font.render(f"ТОП 3 РЕКОРДА:", 0, 'blue')
        record1 = font.render(f"{data[0]}", 0, 'blue')
        record2 = font.render(f"{data[1]}", 0, 'blue')
        record3 = font.render(f"{data[2]}", 0, 'blue')
        f.close()

        screen.blit(main_surface, (0, 0))
        decor_sprites.draw(screen)
        decor_sprites.update()

        screen.blit(button_surface, (435, 200))
        screen.blit(records_text, (1, 0))
        screen.blit(record1, (9, 50))
        screen.blit(record2, (9, 100))
        screen.blit(record3, (9, 150))
        screen.blit(start_text, (480, 215))
        screen.blit(ground_surface, (0, 578))

        screen.blit(quit_but_surface, (435, 350))
        screen.blit(quit_text, (455, 365))
        screen.blit(count_text, (410, 125))

        pygame.display.update()

        clock.tick(20)
