d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.W, Length.short)
d.position_pen(0,1)
d.position_pen(0,2)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.E, Length.medium)

d.end()
