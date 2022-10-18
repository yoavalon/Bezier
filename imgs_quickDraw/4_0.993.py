d = DslBezier()

d.position_pen(1,2)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(3,2)
d.straight_line(Direction.W, Length.medium)

d.end()
