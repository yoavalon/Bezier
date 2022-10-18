d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,2)

d.end()
