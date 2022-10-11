d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.long)
d.position_pen(3,1)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.N, Length.long)
d.position_pen(2,1)

d.end()
