d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.N, Length.short)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.N, Length.medium)

d.end()
