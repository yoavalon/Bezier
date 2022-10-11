d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.N, Length.medium)
d.position_pen(2,2)
d.position_pen(2,1)

d.end()
