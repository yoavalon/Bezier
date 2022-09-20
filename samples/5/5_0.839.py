d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)

d.end()
