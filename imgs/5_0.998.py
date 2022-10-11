d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)

d.end()
