d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,1)

d.end()
