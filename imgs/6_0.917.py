d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.W, Length.medium)
d.position_pen(0,0)
d.straight_line(Direction.SE, Length.long)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,2)

d.end()
