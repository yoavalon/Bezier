d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.N, Orient.right, Length.long, Radius.high)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.position_pen(0,3)
d.position_pen(2,1)

d.end()
