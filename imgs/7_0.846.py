d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)

d.end()
