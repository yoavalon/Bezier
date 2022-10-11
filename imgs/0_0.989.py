d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.position_pen(0,3)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)

d.end()
