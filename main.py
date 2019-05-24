import pygame
import window
import buttons
import workspace
import cleaners as cs
import pymunk
import pymunk.pygame_util


def main():
    screen = window.Screen()
    screen.setup()
    shapes = workspace.WorkSpace(screen)
    shapes.add_floor()
    shapes.init_cursor()

    select_button = buttons.Button(840, 60, 120, 30, 'Select')
    segment_button = buttons.Button(840, 100, 120, 30, 'Line')
    circle_button = buttons.Button(840, 140, 120, 30, 'Circle')
    triangle_button = buttons.Button(840, 180, 120, 30, 'Triangle')
    rect_button = buttons.Button(840, 220, 120, 30, 'Quadrilateral')
    polygon_button = buttons.Button(840, 260, 120, 30, 'Pentagon')
    clear_s = cs.ClearObject(840, 420, 120, 30, 'Clear Lines')
    clear_b = cs.ClearObject(840, 460, 120, 30, 'Clear Balls')
    clear_p = cs.ClearObject(840, 500, 120, 30, 'Clear Polygons')
    clear_a = cs.ClearAll(840, 540, 120, 30, 'Clear All')

    button_list = [select_button, circle_button, segment_button, polygon_button,
                   triangle_button, rect_button, clear_a]

    while screen.running:
        shapes.cursor.body.position = pymunk.pygame_util.from_pygame(pygame.mouse.get_pos(), screen.screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not pygame.mouse.get_pos()[0] > 800:
                    if select_button.activated:
                        if shapes.selected is not None:
                            screen.space.remove(shapes.selected)
                        p = pymunk.pygame_util.from_pygame(pymunk.Vec2d(pygame.mouse.get_pos()), screen.screen)
                        hit = screen.space.point_query_nearest(p, 0, pymunk.ShapeFilter())
                        if hit is not None and type(hit.shape) is not pymunk.shapes.Segment:
                            selected_shape = hit.shape
                            joint = pymunk.PivotJoint(shapes.cursor.body, selected_shape.body, (0, 0), (0, 0))
                            screen.space.add(joint)
                            shapes.selected = joint

            if event.type == pygame.MOUSEBUTTONUP:
                if not pygame.mouse.get_pos()[0] > 800:
                    if shapes.selected is not None:
                        screen.space.remove(shapes.selected)
                        shapes.selected = None

                    if circle_button.activated:
                        shapes.add_ball(pygame.mouse.get_pos())
                    if segment_button.activated:
                        shapes.point_list.append(pygame.mouse.get_pos())
                        if len(shapes.point_list) == 2:
                            shapes.add_segment()
                    if triangle_button.activated:
                        shapes.point_list.append(pygame.mouse.get_pos())
                        if len(shapes.point_list) == 3:
                            shapes.add_poly()
                    if rect_button.activated:
                        shapes.point_list.append(pygame.mouse.get_pos())
                        if len(shapes.point_list) == 4:
                            shapes.add_poly()
                    if polygon_button.activated:
                        shapes.point_list.append(pygame.mouse.get_pos())
                        if len(shapes.point_list) == 5:
                            shapes.add_poly()

                clear_p.activate(pygame.mouse.get_pos(), shapes.poly_list, screen, button_list)
                clear_s.activate(pygame.mouse.get_pos(), shapes.line_list, screen, button_list)
                clear_b.activate(pygame.mouse.get_pos(), shapes.ball_list, screen, button_list)
                for button in button_list:
                    button.activate(pygame.mouse.get_pos(), shapes, screen, button_list)

        clear_p.draw_button(screen, shapes.poly_list)
        clear_s.draw_button(screen, shapes.line_list)
        clear_b.draw_button(screen, shapes.ball_list)
        for button in button_list:
            button.draw_button(screen, shapes)

        screen.draw(shapes)
        screen.space.step(1 / 50.0)
        pygame.time.Clock().tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    main()
