d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NE, Length.long)
d.position_pen(0,3)
d.position_pen(3,1)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,0)

d.end()
