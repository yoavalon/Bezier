d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.S, Length.long)
d.position_pen(3,1)
d.position_pen(2,2)

d.end()
