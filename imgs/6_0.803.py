d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,2)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(3,0)

d.end()
