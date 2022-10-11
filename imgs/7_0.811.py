d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(0,2)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,1)

d.end()
