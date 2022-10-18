d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
