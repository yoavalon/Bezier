d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)

d.end()
