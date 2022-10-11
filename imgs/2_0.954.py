d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.short)
d.position_pen(2,2)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,2)
d.position_pen(0,2)
d.straight_line(Direction.W, Length.long)

d.end()
