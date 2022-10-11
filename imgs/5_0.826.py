d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(3,3)

d.end()
