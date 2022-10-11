d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.N, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.W, Length.medium)

d.end()
