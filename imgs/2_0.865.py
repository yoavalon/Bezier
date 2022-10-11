d = DslBezier()

d.position_pen(2,3)
d.position_pen(3,0)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,3)

d.end()
