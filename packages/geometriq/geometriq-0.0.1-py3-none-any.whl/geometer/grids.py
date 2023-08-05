from math import sqrt

from .shapes import Point, Line


class Grid(object):

    def __init__(self, start, size, iterations_wide, iterations_tall):
        self.start = start
        self.size = float(size)
        self.iterations_wide = iterations_wide + (1 if iterations_wide % size == 0 else 0)
        self.iterations_tall = iterations_tall + (1 if iterations_tall % size == 0 else 0)

        self.points = self._generate_points()

    def _generate_points(self):
        pass

    def _offsets(self, x, y):
        return x, y

    def _mirrored_points(self, x, y, x_idx, y_idx):
        mirror = set()
        x_offset, y_offset = self._offsets(x_idx, y_idx)
        mirror.add(Point(self.start.x + (x + x_offset), self.start.y + (y + y_offset)))
        mirror.add(Point(self.start.x + (x + x_offset), self.start.y - (y + y_offset)))
        mirror.add(Point(self.start.x - (x + x_offset), self.start.y + (y + y_offset)))
        mirror.add(Point(self.start.x - (x + x_offset), self.start.y - (y + y_offset)))

        return mirror

    def closest_point_to(self, other_point):
        distance, point = min([(x.distance_to(other_point), x) for x in self.points])
        return point if distance < 0.05 * self.size else other_point

    def radial_sort(self, center):
        points = list(self.points)
        return sorted(points, cmp=lambda a, b: cmp(a.distance_to(center), b.distance_to(center)))

    def linear_sort(self, line):
        points = list(self.points)
        if line.slope is None:  # vertical line shortcut
            sorted_points = sorted(points, lambda a, b: cmp(abs(a.x - line.center.x), abs(b.x - line.center.x)))
        elif line.slope == 0:  # horizontal line shortcut
            sorted_points = sorted(points, lambda a, b: cmp(abs(a.y - line.center.y), abs(b.y - line.center.y)))
        else:
            sorted_points = sorted(points, lambda a, b: cmp(line.distance_to(a), line.distance_to(b)))

        return sorted_points


class SquareGrid(Grid):
    """ A grid of points arranged in squares.

    >>> square_grid = SquareGrid(Point(5.0, 5.0), 1, 1, 1)
    >>> len(square_grid.points)
    9
    >>> Point(4, 6) in square_grid.points
    True
    >>> Point(5, 6) in square_grid.points
    True
    >>> Point(6, 6) in square_grid.points
    True
    >>> Point(4, 5) in square_grid.points
    True
    >>> Point(5, 5) in square_grid.points
    True
    >>> Point(6, 5) in square_grid.points
    True
    >>> Point(4, 4) in square_grid.points
    True
    >>> Point(5, 4) in square_grid.points
    True
    >>> Point(6, 4) in square_grid.points
    True
    >>> Point(3, 3) in square_grid.points
    False
    """

    def _generate_points(self):
        points = set()

        for y in range(self.iterations_tall):
            for x in range(self.iterations_wide):

                p_x = x * self.size
                p_y = y * self.size

                points.update(self._mirrored_points(p_x, p_y, x, y))

        return points


class DiamondGrid(Grid):
    """ A grid of points arranged in diamonds (squares, rotated 45 degrees).

    """

    def __init__(self, start, size, iterations_wide, iterations_tall):
        self.step = sqrt(size**2 / 2)
        super(DiamondGrid, self).__init__(start, size, iterations_wide, iterations_tall)

    def _generate_points(self):
        points = set()

        for y in range(self.iterations_tall):
            for x in range(self.iterations_wide):

                p_x = x * self.step
                y_offset = 0 if x % 2 == 0 else self.step
                p_y = y * self.step - y_offset
                
                points.update(self._mirrored_points(p_x, p_y, x, y))

        return points


class HorizontalHexagonGrid(Grid):
    """ A grid of points arranged in equilateral triangles, aligned horizontally.

    """

    def __init__(self, start, size, iterations_wide, iterations_tall):
        self.step = sqrt(size**2 - (size / 2)**2)
        self.r = sqrt(3) * size / 6
        super(HorizontalHexagonGrid, self).__init__(start, size, iterations_wide, iterations_tall)

    def _offsets(self, x, y):
        y_offset = y * self.step
        y_offset += 0 if x % 2 == 0 else self.step
        return x, y_offset

    def _generate_points(self):
        points = set()

        for y in range(self.iterations_tall):
            for x in range(self.iterations_wide):

                p_x = x * (self.size / 2)
                p_y = y * self.step

                points.update(self._mirrored_points(p_x, p_y, x, y))

        return points


class VerticalHexagonGrid(Grid):
    """ A grid of points arranged in equilateral triangles, aligned vertically.

    """

    def __init__(self, start, size, iterations_wide, iterations_tall):
        self.step = sqrt(size ** 2 - (size / 2) ** 2)
        self.r = sqrt(3) * size / 6
        super(VerticalHexagonGrid, self).__init__(start, size, iterations_wide, iterations_tall)

    def _offsets(self, x, y):
        y_offset = y * (self.size / 2)
        y_offset += 0 if x % 2 == 0 else (self.size / 2)
        return x, y_offset

    def _generate_points(self):
        points = set()

        for y in range(self.iterations_tall):
            for x in range(self.iterations_wide):

                p_x = x * self.step
                p_y = y * (self.size / 2)

                points.update(self._mirrored_points(p_x, p_y, x, y))

        return points
