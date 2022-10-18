d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.short)
d.position_pen(0,1)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)

d.end()
