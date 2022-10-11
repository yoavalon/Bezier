d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.NE, Length.medium)

d.end()
