d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,0)
d.straight_line(Direction.NE, Length.medium)

d.end()
