d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.W, Length.long)
d.position_pen(2,0)

d.end()
