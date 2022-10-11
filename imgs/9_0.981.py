d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.position_pen(0,2)
d.straight_line(Direction.E, Length.medium)

d.end()
