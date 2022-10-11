d = DslBezier()

d.position_pen(1,3)
d.position_pen(3,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.long)

d.end()
