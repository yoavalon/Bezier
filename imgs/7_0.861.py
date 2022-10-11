d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)

d.end()
