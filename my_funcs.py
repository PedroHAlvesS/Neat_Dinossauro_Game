import os
import pygame


def load_sprite_sheet_img():
    current = os.path.dirname(__file__)
    img_dir = os.path.join(current, 'imgs')
    sprite_sheet_dir = os.path.join(img_dir, 'dinoSpritesheet.png')
    sprit_sheet = pygame.image.load(sprite_sheet_dir).convert_alpha()
    return sprit_sheet


def load_dino_sprite_sheet_img():
    sprit_sheet = load_sprite_sheet_img()
    dino_sprite_sheet_img = list()
    sprite_x_width = 32
    for i in range(3):
        sprit_x = i * sprite_x_width
        img = sprit_sheet.subsurface((sprit_x, 0), (32, 32))
        img_transform = pygame.transform.scale(img, (32 * 3, 32 * 3))
        dino_sprite_sheet_img.append(img_transform)
    return dino_sprite_sheet_img
