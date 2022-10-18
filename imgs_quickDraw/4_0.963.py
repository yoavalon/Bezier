d = DslBezier()

d.position_pen(3,2)
d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,3)

d.end()
