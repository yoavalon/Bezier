d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,3)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.E, Length.short)

d.end()
