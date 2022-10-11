d = DslBezier()

d.position_pen(2,2)
d.position_pen(3,2)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
