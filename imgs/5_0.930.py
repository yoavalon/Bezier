d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)

d.end()
