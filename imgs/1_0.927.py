d = DslBezier()

d.position_pen(1,1)
d.position_pen(0,3)
d.straight_line(Direction.SW, Length.long)
d.position_pen(3,3)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.position_pen(0,1)

d.end()
