d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.S, Length.short)
d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.position_pen(2,2)

d.end()
