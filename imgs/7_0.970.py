d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,1)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)

d.end()
