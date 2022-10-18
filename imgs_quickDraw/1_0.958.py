d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.short)
d.position_pen(2,0)

d.end()
