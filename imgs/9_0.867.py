d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)

d.end()
