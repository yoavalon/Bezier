d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,0)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NW, Length.medium)

d.end()
