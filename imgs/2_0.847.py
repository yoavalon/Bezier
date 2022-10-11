d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,1)
d.position_pen(0,1)

d.end()
