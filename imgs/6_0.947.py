d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.medium)
d.position_pen(3,1)
d.straight_line(Direction.N, Length.long)

d.end()
