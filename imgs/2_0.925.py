d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.E, Length.short)
d.position_pen(2,0)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
