d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)

d.end()
