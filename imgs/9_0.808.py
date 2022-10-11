d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,3)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,0)
d.straight_line(Direction.S, Length.long)

d.end()
