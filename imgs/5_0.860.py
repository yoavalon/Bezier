d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,3)
d.straight_line(Direction.E, Length.short)

d.end()
