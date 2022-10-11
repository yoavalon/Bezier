d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.position_pen(3,3)
d.straight_line(Direction.N, Length.medium)

d.end()
