d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(0,2)
d.position_pen(0,1)
d.straight_line(Direction.E, Length.short)

d.end()
