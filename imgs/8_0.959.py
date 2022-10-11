d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.NE, Length.long)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.position_pen(3,2)

d.end()
