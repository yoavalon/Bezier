d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.position_pen(0,0)
d.position_pen(1,3)
d.position_pen(3,2)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
