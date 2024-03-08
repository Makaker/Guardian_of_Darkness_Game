import pygame
from manager_screen import ManagerScreen
from setting import *
from event_management import EventManagement
from main_menu import MainMenu

pygame.init()

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Guardian of Darkness')

clock = pygame.time.Clock()

manager_screen = ManagerScreen(screen)
main_menu = MainMenu(screen)
event_management = EventManagement(screen, main_menu.get_buttons())  # принимает из главного меню список кнопок

while True:
    # отслеживает все события
    event_management.main_event()

    clock.tick(FPS)
    screen.fill(bg_color_star)

    manager_screen.screen_selection()
    manager_screen.draw()

    main_menu.button_new_game.on_click()
    main_menu.button_load_game.on_click()
    main_menu.button_exit_game.on_click()

    pygame.display.update()
