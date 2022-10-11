d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.N, Length.medium)

d.end()
