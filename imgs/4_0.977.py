d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,0)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.NW, Length.long)
d.position_pen(0,1)

d.end()
