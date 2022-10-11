d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.position_pen(0,0)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.long)

d.end()
