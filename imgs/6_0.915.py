d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.short)
d.position_pen(2,3)

d.end()
