d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.NE, Length.medium)

d.end()
