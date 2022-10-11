d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.S, Length.long)
d.position_pen(2,1)

d.end()
