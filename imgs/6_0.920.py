d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,0)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)

d.end()
