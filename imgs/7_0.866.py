d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.low)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.short)

d.end()
