d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.NE, Length.medium)

d.end()
