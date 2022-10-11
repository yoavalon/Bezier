d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.short)

d.end()
