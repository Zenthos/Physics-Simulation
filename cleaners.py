import pygame
import pymunk
from buttons import Button


class ClearObject(Button):
    def __init__(self, x, y, w, h, text):
        Button.__init__(self, x, y, w, h, text)
        self.active_color = (110, 110, 110)

    def activate(self, mouse, object_list,  screen, button_list):
        x = mouse[0]
        y = mouse[1]
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height and not self.activated:
            self.activated = True
            self.clear_object(object_list, screen)

    def clear_object(self, object_list, screen):
        if self.activated:
            self.activated = False
            while object_list:
                for obj in object_list:
                    object_list.remove(obj)
                    if obj.body == pymunk.Body.STATIC:
                        screen.space.remove(obj, obj.body)
                    else:
                        screen.space.remove(obj)

    def draw_button(self, screen, object_list):
        if object_list:
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


class ClearAll(Button):
    def __init__(self, x, y, w, h, text):
        Button.__init__(self, x, y, w, h, text)
        self.active_color = (110, 110, 110)

    def activate(self, mouse, shapes,  screen, button_list):
        x = mouse[0]
        y = mouse[1]
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height and not self.activated:
            self.activated = True
            self.clear_all(shapes, screen)

    def clear_all(self, shapes, screen):
        if self.activated:
            shapes.point_list.clear()
            self.activated = False
            while shapes.poly_list or shapes.line_list or shapes.ball_list:
                for polygon in shapes.poly_list:
                    shapes.poly_list.remove(polygon)
                    screen.space.remove(polygon, polygon.body)
                for line in shapes.line_list:
                    shapes.line_list.remove(line)
                    screen.space.remove(line)
                for ball in shapes.ball_list:
                    shapes.ball_list.remove(ball)
                    screen.space.remove(ball, ball.body)

    def draw_button(self, screen, shapes):
        if shapes.line_list or shapes.ball_list or shapes.poly_list:
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
