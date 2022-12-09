from aocd import data, lines, submit


# lines = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2""".split(
#     "\n"
# )

# lines = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20""".split(
#     "\n"
# )


class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Knot(Coordinate):
    def __init__(self):
        super(Knot, self).__init__()
        self.visited = set()
        self.visit()
        self.actions = {}
        self.register_actions()

    def visit(self):
        self.visited.add((self.x, self.y))

    def distance(self, coord: Coordinate):
        return max([abs(coord.x - self.x), abs(coord.y - self.y)])

    def direction(self, coord: Coordinate):
        lr = coord.x - self.x
        lr = lr if lr == 0 else lr / abs(lr)
        ud = coord.y - self.y
        ud = ud if ud == 0 else ud / abs(ud)
        return (lr, ud)

    def up(self, steps=1):
        self.y += steps

    def down(self, steps=1):
        self.y -= steps

    def right(self, steps=1):
        self.x += steps

    def left(self, steps=1):
        self.x -= steps

    def register_actions(self):
        self.actions = {"R": self.right, "U": self.up, "D": self.down, "L": self.left}

    def follow(self, coord: Coordinate):
        while self.distance(coord) > 1:
            lr, up = self.direction(coord)
            if lr == 1:
                self.right()
            elif lr == -1:
                self.left()

            if up == 1:
                self.up()
            elif up == -1:
                self.down()
            self.visit()


def pt1():
    h = Knot()
    t = Knot()
    for line in lines:
        action, steps = tuple(line.split())
        h.actions[action](int(steps))
        t.follow(h)
    print(len(t.visited))
    submit(len(t.visited))


def pt2():
    rope = [Knot() for _ in range(10)]
    for line in lines:
        action, steps = tuple(line.split())
        for _ in range(int(steps)):
            rope[0].actions[action]()
            for idx in range(len(rope) - 1):
                rope[idx + 1].follow(rope[idx])
    print(len(rope[-1].visited))
    submit(len(rope[-1].visited))


if __name__ == "__main__":
    # pt1()
    pt2()
