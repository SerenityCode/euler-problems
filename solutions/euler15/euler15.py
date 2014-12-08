# Lattice paths https://projecteuler.net/problem=15
# Starting in the top left corner of a 2x2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?
gridSize = 20


def pathing(point):
    if point == [0, 0]:
        return 1
    steps = 0
    if point[0] > 0:
        steps += pathing([point[0]-1, point[1]])
    if point[1] > 0:
        steps += pathing([point[0], point[1]-1])
    return steps

print pathing([gridSize, gridSize])
# This is super super slow and I'm sure
# there are millions of better ways to do it