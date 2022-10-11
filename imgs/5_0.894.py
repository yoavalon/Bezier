d = DslBezier()

d.position_pen(3,1)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.position_pen(1,3)

d.end()
