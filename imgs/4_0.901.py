d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,1)
d.position_pen(1,3)

d.end()
