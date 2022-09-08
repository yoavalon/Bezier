d = DslBezier()

d.position_pen(2,2)
d.position_pen(1,3)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,1)
d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
