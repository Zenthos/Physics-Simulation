import pygame
import sys
import pymunk
import pymunk.pygame_util
pygame.init()


class Screen:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.running = True
        self.font = pygame.font.SysFont("Arial", 16)
        self.space = pymunk.Space()

    def setup(self):
        self.screen.fill((100, 100, 100))
        self.space.gravity = (0.0, -900.0)
        self.font.set_bold(True)
        pygame.display.set_caption("Drawing Shapes")

    def draw(self, shapes):
        pygame.draw.rect(self.screen, (26, 26, 29), (0, 0, 800, 600), 0)

        for ball in shapes.ball_list:
            p = pymunk.pygame_util.to_pygame(ball.body.position, self.screen)
            pygame.draw.circle(self.screen, (197, 198, 199), p, int(ball.radius), 0)

        for line in shapes.line_list:
            point1 = pymunk.pygame_util.to_pygame(line.a, self.screen)
            point2 = pymunk.pygame_util.to_pygame(line.b, self.screen)
            pygame.draw.line(self.screen, (255, 255, 255), point1, point2, 3)

        for poly in shapes.poly_list:
            vertices = [point.rotated(poly.body.angle) + poly.body.position for point in poly.get_vertices()]
            vertices = [pymunk.pygame_util.to_pygame(point, self.screen) for point in vertices]
            pygame.draw.polygon(self.screen, (64, 86, 161), vertices, 0)

        for point in shapes.point_list:
            pygame.draw.circle(self.screen, (255, 255, 255), point, 3, 0)
            if len(shapes.point_list) > 1:
                pygame.draw.lines(self.screen, (255, 255, 255), False, shapes.point_list, 3)

        if pygame.mouse.get_pos()[0] < 800:
            pygame.draw.circle(self.screen, (255, 255, 255), pygame.mouse.get_pos(), 3, 0)

        pygame.draw.rect(self.screen, (60, 60, 60), (800, 0, 200, 600), 0)
        flr = pymunk.pygame_util.to_pygame(shapes.floor_shape.body.position, self.screen)
        rect = flr[0], flr[1] - 49, 800, 50
        pygame.draw.rect(self.screen, (31, 40, 53), rect, 0)

    def exit(self):
        self.running = False
        pygame.quit()
        sys.exit()
