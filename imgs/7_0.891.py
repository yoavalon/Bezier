d = DslBezier()

d.position_pen(1,2)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.N, Length.medium)

d.end()
