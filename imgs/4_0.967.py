d = DslBezier()

d.position_pen(1,1)
d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)

d.end()
