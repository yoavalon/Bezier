d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)
d.position_pen(2,1)

d.end()
