d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,1)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,3)
d.straight_line(Direction.N, Length.long)

d.end()
