d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.S, Length.short)
d.position_pen(3,2)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(2,1)

d.end()
