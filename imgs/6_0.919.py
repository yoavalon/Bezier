d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,1)
d.straight_line(Direction.S, Length.medium)

d.end()
