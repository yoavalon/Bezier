d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.W, Length.medium)
d.position_pen(0,3)

d.end()
