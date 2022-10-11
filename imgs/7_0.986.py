d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(3,2)
d.position_pen(1,0)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,0)

d.end()
