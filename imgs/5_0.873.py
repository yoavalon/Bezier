d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.position_pen(0,2)

d.end()
