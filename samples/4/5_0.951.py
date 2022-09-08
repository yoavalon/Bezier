d = DslBezier()

d.position_pen(0,2)
d.position_pen(3,1)
d.position_pen(0,0)
d.straight_line(Direction.SW, Length.long)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.S, Length.short)

d.end()
