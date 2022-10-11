d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,1)
d.straight_line(Direction.NE, Length.short)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)

d.end()
