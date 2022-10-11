d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.E, Length.medium)

d.end()
