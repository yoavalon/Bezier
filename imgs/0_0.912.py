d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.position_pen(3,0)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)

d.end()
