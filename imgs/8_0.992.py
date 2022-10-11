d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.E, Length.medium)

d.end()
