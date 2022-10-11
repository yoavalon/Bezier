d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,2)
d.position_pen(2,3)
d.position_pen(1,1)
d.straight_line(Direction.NW, Length.medium)

d.end()
