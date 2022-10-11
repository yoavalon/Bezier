d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.N, Orient.left, Length.short, Radius.high)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.S, Length.long)
d.position_pen(2,3)

d.end()
