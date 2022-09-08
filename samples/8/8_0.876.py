d = DslBezier()

d.position_pen(0,2)
d.position_pen(2,3)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)
d.position_pen(3,2)
d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.W, Length.medium)

d.end()
