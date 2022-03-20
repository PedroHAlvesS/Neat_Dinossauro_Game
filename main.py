import pygame
import os
from button import Button


def load_config():
    height = 500
    width = 800

    fps = 30

    config = dict()
    config['height'] = height
    config['width'] = width
    config['fps'] = fps
    return config


def create_screen():
    config = load_config()
    width = config['width']
    height = config['height']
    screen = pygame.display.set_mode((width, height))
    return screen


def load_button_config(window_height, window_width):
    # botton config
    color = (255, 153, 153)
    outline_color = (0, 0, 0) # black RGB
    width_button = 250
    height_button = 70
    button_x = (window_width / 2) - (width_button / 2)
    button_y = (window_height / 2)
    # place config in a dict
    button_config = dict()
    button_config['color'] = color
    button_config['outline_color'] = outline_color
    button_config['width_button'] = width_button
    button_config['height_button'] = height_button
    button_config['button_x'] = button_x
    button_config['button_y'] = button_y
    return button_config


def create_buttons(window_height, window_width):
    # load botton config
    button_config = load_button_config(window_height=window_height, window_width=window_width)

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


def draw_window(window, bg, buttons):
    pygame.display.update()
    window.blit(bg, (0, 0))
    buttons['player'].draw(win=window)
    buttons['ai'].draw(win=window)
    buttons['player_vs_ai'].draw(win=window)


def menu_loop(window):
    # load configs
    configs = load_config()
    # load Background
    bg = pygame.image.load(os.path.join('imgs', 'menu.jpg'))
    # load bottons
    width = configs['width']
    height = configs['height']
    buttons = create_buttons(window_height=height, window_width=width)

    menu_running = True
    while menu_running:
        fps = configs['fps']
        CLOCK.tick(fps)
        # draw screen
        draw_window(window=window, bg=bg, buttons=buttons)

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
    # configs
    pygame.init()
    pygame.display.set_caption("Dino Menu")

    WINDOW = create_screen()

    CLOCK = pygame.time.Clock()

    menu_loop(window=WINDOW)
