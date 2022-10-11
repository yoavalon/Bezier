d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(3,0)
d.position_pen(1,1)
d.straight_line(Direction.NW, Length.long)

d.end()
