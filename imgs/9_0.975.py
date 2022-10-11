d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)
d.position_pen(1,2)

d.end()
