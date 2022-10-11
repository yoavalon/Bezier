d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.E, Length.short)
d.position_pen(3,1)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,0)

d.end()
