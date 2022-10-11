d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.position_pen(1,0)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)

d.end()
