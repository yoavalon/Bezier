d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.short)

d.end()
