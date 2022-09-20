d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.N, Length.long)
d.position_pen(2,3)

d.end()
