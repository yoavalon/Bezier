d = DslBezier()

d.position_pen(0,1)
d.position_pen(1,2)
d.straight_line(Direction.SW, Length.short)
d.position_pen(1,3)
d.position_pen(2,2)

d.end()
