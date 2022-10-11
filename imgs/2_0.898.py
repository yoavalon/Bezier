d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,3)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,2)

d.end()
