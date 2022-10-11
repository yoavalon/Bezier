d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.NW, Length.long)
d.position_pen(0,2)
d.straight_line(Direction.NE, Length.long)

d.end()
