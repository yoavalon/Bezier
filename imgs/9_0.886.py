d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.W, Length.long)
d.position_pen(2,0)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.position_pen(1,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.position_pen(2,3)

d.end()
