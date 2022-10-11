d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.medium)

d.end()
