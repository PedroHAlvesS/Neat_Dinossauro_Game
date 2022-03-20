import main
import models
import pygame
from pygame.locals import *


def create_sprite_dino():
    sprit_group = pygame.sprite.Group()
    dino = models.Dino()
    sprit_group.add(dino)
    return sprit_group


def draw_window(window, sprite_dino_group):
    sprite_dino_group.draw(window)
    sprite_dino_group.update()
    pygame.display.flip()


def game_loop(window):
    sprite_dino_group = create_sprite_dino()
    white_color = (255, 255, 255) # white in rgb
    running = True
    while running:
        window.fill(white_color)
        CLOCK.tick(30)
        draw_window(window=window, sprite_dino_group=sprite_dino_group)
        # User interaction
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Dino Game - Player")

    window = main.create_screen()
    CLOCK = pygame.time.Clock()
    game_loop(window)
