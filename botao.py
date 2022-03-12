import pygame


class Button:
    def __init__(self, color, x, y, width, height, text='', outline=None):
        self.__color = color
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__text = text
        self.__outline = outline

    def draw(self, win):
        # Call this method to draw the button on the screen
        if self.__outline:
            pygame.draw.rect(win, self.__outline, (self.__x - 2, self.__y - 2, self.__width + 4, self.__height + 4), 0)

        pygame.draw.rect(win, self.__color, (self.__x, self.__y, self.__width, self.__height), 0)

        if self.__text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.__text, True, (0, 0, 0))
            win.blit(text, (self.__x + (self.__width / 2 - text.get_width() / 2),
                            self.__y + (self.__height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.__x < pos[0] < self.__x + self.__width:
            if self.__y < pos[1] < self.__y + self.__height:
                return True
        return False
