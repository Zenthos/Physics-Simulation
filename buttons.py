import pygame


class Button:
    def __init__(self, x, y, w, h, text):
        self.border = (0, 0, 0)
        self.color = (172, 59, 97)
        self.active_color = (255, 40, 0)
        self.text_color = (255, 255, 255)
        self.text = text
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.activated = False

    def activate(self, mouse,  shapes, space, button_list):
        x = mouse[0]
        y = mouse[1]
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height and not self.activated:
            for button in button_list:
                button.activated = False
            shapes.point_list.clear()
            self.activated = True
        elif self.x < x < self.x + self.width and self.y < y < self.y + self.height and self.activated:
            shapes.point_list.clear()
            self.activated = False

    def draw_button(self, screen, shapes):
        if not self.activated:
            pygame.draw.rect(screen.screen, self.color, (self.x, self.y, self.width, self.height), 0)
            pygame.draw.rect(screen.screen, self.border, (self.x, self.y, self.width, self.height), 3)
            button_text = screen.font.render(self.text, True, self.text_color)
            text_rect = button_text.get_rect(center=(self.x + (self.width/2), self.y + (self.height/2)))
            screen.screen.blit(button_text, text_rect)
        else:
            pygame.draw.rect(screen.screen, self.active_color, (self.x, self.y, self.width, self.height), 0)
            pygame.draw.rect(screen.screen, self.border, (self.x, self.y, self.width, self.height), 3)
            button_text = screen.font.render(self.text, True, self.text_color)
            text_rect = button_text.get_rect(center=(self.x + (self.width/2), self.y + (self.height/2)))
            screen.screen.blit(button_text, text_rect)
