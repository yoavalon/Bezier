d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.position_pen(1,1)
d.straight_line(Direction.N, Length.long)

d.end()
