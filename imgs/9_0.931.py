d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.position_pen(2,2)

d.end()
