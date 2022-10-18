d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.N, Orient.left, Length.short, Radius.low)
d.position_pen(0,2)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.NE, Length.short)

d.end()
