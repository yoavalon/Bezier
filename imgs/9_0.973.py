d = DslBezier()

d.position_pen(2,0)
d.position_pen(2,2)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.position_pen(3,2)

d.end()
