import math


def validSquare(p1, p2, p3, p4):
    if (0 < dis(p1, p2) == dis(p3, p4) > 0 and
        (parallel([p1[0] - p2[0], p1[1] - p2[1]], [p3[0] - p4[0], p3[1] - p4[1]])
         or vertical([p1[0] - p2[0], p1[1] - p2[1]], [p3[0] - p4[0], p3[1] - p4[1]]))) \
            and \
            (0 < dis(p1, p3) == dis(p2, p4 > 0)
             and (parallel([p1[0] - p3[0], p1[1] - p3[1]], [p2[0] - p4[0], p2[1] - p4[1]])
                  or vertical([p1[0] - p3[0], p1[1] - p3[1]], [p2[0] - p4[0], p2[1] - p4[1]]))) \
            and \
            (0 < dis(p1, p4) == dis(p2, p3 > 0)
             and (parallel([p1[0] - p4[0], p1[1] - p4[1]], [p2[0] - p3[0], p2[1] - p3[1]])
                  or vertical([p1[0] - p4[0], p1[1] - p4[1]], [p2[0] - p3[0], p2[1] - p3[1]]))):
        return True
    else:
        return False


def dis(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def parallel(a, b):
    if a[1] * b[0] == b[1] * a[0]:
        return True
    else:
        return False


def vertical(a, b):
    if a[0] * b[0] + a[1] * b[1] == 0:
        return True
    else:
        return False


print(validSquare([0, 0], [5, 0], [5, 4], [0, 4]))
