import pygame
import os
from botao import Button

# configs
pygame.init()

HEIGHT = 500
WIDTH = 800

FPS = 30

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino")

CLOCK = pygame.time.Clock()


def load_button_config(screen_height, screen_width):
    # botton config
    color = (255, 153, 153)
    outline_color = (0, 0, 0)
    width_button = 250
    height_button = 70
    button_x = (screen_width / 2) - (width_button / 2)
    button_y = (screen_height / 2)
    # place config in a dict
    button_config = dict()
    button_config['color'] = color
    button_config['outline_color'] = outline_color
    button_config['width_button'] = width_button
    button_config['height_button'] = height_button
    button_config['button_x'] = button_x
    button_config['button_y'] = button_y
    return button_config


def create_buttons(screen_height, screen_width):
    # load botton config
    button_config = load_button_config(screen_height=screen_height, screen_width=screen_width)

    # create the buttons
    player_button_option = Button(color=button_config['color'], x=button_config['button_x'],
                                  y=button_config['button_y'], width=button_config['width_button'],
                                  height=button_config['height_button'], text="Player",
                                  outline=button_config['outline_color'])
    ai_button_option = Button(color=button_config['color'], x=button_config['button_x'],
                              y=button_config['button_y'] + 80, width=button_config['width_button'],
                              height=button_config['height_button'], text="Ai Train",
                              outline=button_config['outline_color'])
    player_ai_button_option = Button(color=button_config['color'], x=button_config['button_x'],
                                     y=button_config['button_y'] + 160, width=button_config['width_button'],
                                     height=button_config['height_button'], text="Player Vs Ai",
                                     outline=button_config['outline_color'])

    # Place the create buttons in a dict
    buttons = dict()
    buttons['player'] = player_button_option
    buttons['ai'] = ai_button_option
    buttons['player_vs_ai'] = player_ai_button_option

    return buttons


def draw_screen(screen, bg, buttons):
    pygame.display.update()
    screen.blit(bg, (0, 0))
    buttons['player'].draw(win=screen)
    buttons['ai'].draw(win=screen)
    buttons['player_vs_ai'].draw(win=screen)


def menu_loop(screen):
    # load Background
    bg = pygame.image.load(os.path.join('imgs', 'bg_800_500.jpg'))
    # load bottons
    buttons = create_buttons(screen_height=HEIGHT, screen_width=WIDTH)

    menu_running = True
    while menu_running:
        CLOCK.tick(FPS)
        # draw screen
        draw_screen(screen=screen, bg=bg, buttons=buttons)

        # User interaction
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                menu_running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_running = False
                    pygame.quit()
            # buttons click
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if buttons['player'].isOver(pos):
                    print("Opçao Player")
                elif buttons['ai'].isOver(pos):
                    print("Opçao Ai")
                elif buttons['player_vs_ai'].isOver(pos):
                    print("Player vs Ai")


if __name__ == "__main__":
    menu_loop(screen=SCREEN)
