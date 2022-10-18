d = DslBezier()

d.position_pen(0,0)
d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.position_pen(2,3)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.medium)

d.end()
