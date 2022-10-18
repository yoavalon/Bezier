d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,1)
d.curve(Direction.N, Orient.right, Length.long, Radius.high)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)

d.end()
