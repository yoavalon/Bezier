d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.E, Length.long)
d.position_pen(0,1)
d.position_pen(2,0)

d.end()
