d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)

d.end()
