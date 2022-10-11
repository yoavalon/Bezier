d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,3)

d.end()
