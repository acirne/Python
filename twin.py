for y in range(12,99):
    yStr = str(y)
    yReverse = "".join(reversed(yStr))
    t = int(yReverse)
    r = t - y
    print("{} {} {}".format(y, t, r))
