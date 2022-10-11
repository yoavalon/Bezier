d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)

d.end()
