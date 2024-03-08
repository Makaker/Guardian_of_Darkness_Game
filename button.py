import pygame
from setting import *


class Button:
    def __init__(self, screen, x, y, text, image_path, hover_image_path=None, font_path=None, event_manager=None):
        self.font_path = font_path
        self.screen = screen
        self.x = x
        self.y = y
        self.text = text

        self.image = pygame.image.load(image_path)
        self.hover_image = pygame.image.load(hover_image_path)
        self.rect_image = self.image.get_rect(topleft=(x, y))

        # для отслеживания конкретных кнопок, создаем поверхности и ставим их на кнопки которые нам нужны
        self.image_button_exit = pygame.surface.Surface((200, 100))
        self.image_button_exit_rect = self.image_button_exit.get_rect(topleft=((W // 2) - 100, (H - (H - 320))))

        self.image_button_new_game = pygame.surface.Surface((200, 100))
        self.image_button_new_game_rect = self.image_button_new_game.get_rect(topleft=((W // 2) - 100, (H - (H - 100))))

        # флаг для наведения
        self.is_hover = False
        self.is_hover_exit_button = False
        self.event_manager = event_manager

    # проверка на навидение курсора мыши рект кнопки
    def check_hover(self, mouse_pos):
        self.is_hover = self.rect_image.collidepoint(mouse_pos)
        return self.is_hover

    def drow(self):
        # текущее изображение что бы при наведении менялись кнопки если флаг
        # если наведение есть:
        if self.is_hover:
            # текущее изображение = изображение наведенной кнопки
            current_image = self.hover_image
        else:
            # впротивном случае = изображению обычной кнопки
            current_image = self.image
        # и отрисовываем кнопку текущей ситуации
        self.screen.blit(current_image, self.rect_image)

        # отрисовка текста на
        font = pygame.font.Font(self.font_path, 30)
        text_button = font.render(self.text, True, (button_text_color))
        # отрисовывается текст на ректе текущей кнопки
        text_rect = text_button.get_rect(center=self.rect_image.center)
        self.screen.blit(text_button, text_rect)

    # отслеживание наведения на кнопку новая игра
    def check_new_game(self, mouse_pos):
        self.is_hover = self.image_button_new_game_rect.collidepoint(mouse_pos)
        return self.is_hover

    # отслеживание на навидение кнопки выхода
    def check_exit(self, mouse_pos):
        self.is_hover = self.image_button_exit_rect.collidepoint(mouse_pos)
        return self.is_hover
    # !!! загадочный момент но пвоспроизводит звук при наведении и якобы нажатии кнопки мыши
    def on_click(self):
        if self.is_hover and self.event_manager:
            self.event_manager.play_button_sound()
