d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.position_pen(0,2)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.short)

d.end()
