d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,2)

d.end()
