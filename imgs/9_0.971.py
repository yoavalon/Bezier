d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,0)

d.end()
