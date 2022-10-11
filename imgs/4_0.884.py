d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)

d.end()
