d = DslBezier()

d.position_pen(1,2)
d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.position_pen(0,0)
d.straight_line(Direction.NE, Length.medium)

d.end()
