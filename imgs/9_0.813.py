d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.position_pen(2,1)

d.end()
