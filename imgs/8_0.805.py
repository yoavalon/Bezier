d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,1)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.short)

d.end()
