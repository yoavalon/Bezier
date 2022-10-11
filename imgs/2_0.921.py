d = DslBezier()

d.position_pen(1,0)
d.position_pen(1,0)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)

d.end()
