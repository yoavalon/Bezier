d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,1)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,2)

d.end()
