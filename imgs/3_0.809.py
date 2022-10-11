d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.long, Radius.high)
d.position_pen(0,2)
d.straight_line(Direction.W, Length.medium)

d.end()
