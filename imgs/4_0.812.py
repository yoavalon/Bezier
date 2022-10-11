d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.S, Length.short)

d.end()
