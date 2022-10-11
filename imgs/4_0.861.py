d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,2)
d.straight_line(Direction.N, Length.short)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)

d.end()
