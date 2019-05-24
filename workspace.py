import pymunk
import pymunk.pygame_util
import pymunk.util as pu


class WorkSpace:
    def __init__(self, surface):
        self.screen = surface.screen
        self.space = surface.space
        self.point_list = []
        self.poly_list = []
        self.ball_list = []
        self.line_list = []
        self.floor_shape = None
        self.selected = None
        self.cursor = None

    def init_cursor(self):
        radius = 3
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.cursor = pymunk.Circle(body, radius, (0, 0))
        self.space.add(body, self.cursor)

    def add_floor(self):
        vertices = [(0, 0), (800, 0), (800, 50), (0, 50)]
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = self._to_pymunk((0, 600))
        shape = pymunk.Poly(body, vertices)
        shape.elasticity = 0.95
        self.space.add(body, shape)
        self.floor_shape = shape

    def add_segment(self):
        point1 = self._to_pymunk(self.point_list[0])
        point2 = self._to_pymunk(self.point_list[1])
        shape = pymunk.Segment(self.space.static_body, point1, point2, 3)
        shape.elasticity = 0.95
        self.space.add(shape)
        self.line_list.append(shape)
        self.point_list.clear()

    def add_ball(self, position):
        mass = 1
        radius = 20
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        body = pymunk.Body(mass, inertia)
        body.position = self._to_pymunk(position)
        shape = pymunk.Circle(body, radius, (0, 0))
        shape.elasticity = 0.95
        self.space.add(body, shape)
        self.ball_list.append(shape)
        self.point_list.clear()

    def add_poly(self):
        mass = 10
        self.point_list = [self._to_pymunk(point) for point in self.point_list]
        center = pu.calc_center(self.point_list)
        vertices = pu.poly_vectors_around_center(self.point_list)
        inertia = pymunk.moment_for_poly(mass, vertices)
        if inertia < 0:
            print("Invalid Points")
            return
        body = pymunk.Body(mass, inertia)
        body.position = center
        shape = pymunk.Poly(body, vertices)
        shape.elasticity = 0.3
        self.space.add(body, shape)
        self.poly_list.append(shape)
        self.point_list.clear()

    def _to_pymunk(self, vector):
        return pymunk.pygame_util.from_pygame(vector, self.screen)
