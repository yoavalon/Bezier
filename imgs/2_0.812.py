d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)

d.end()
