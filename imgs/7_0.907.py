d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(0,2)

d.end()
