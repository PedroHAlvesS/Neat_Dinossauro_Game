import pygame
import my_funcs


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__image_dino_sprites = my_funcs.load_dino_sprite_sheet_img()
        self.__image_index = 0
        self.image = self.__image_dino_sprites[self.__image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def update(self):
        self.__image_index += 0.25
        if self.__image_index >= len(self.__image_dino_sprites):
            self.__image_index = 0
        self.image = self.__image_dino_sprites[int(self.__image_index)]
