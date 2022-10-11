d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.N, Length.medium)
d.position_pen(3,3)
d.position_pen(0,1)
d.straight_line(Direction.SE, Length.short)

d.end()
