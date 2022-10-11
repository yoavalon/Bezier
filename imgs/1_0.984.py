d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)

d.end()
