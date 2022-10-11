d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.NW, Length.medium)

d.end()
