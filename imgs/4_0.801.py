d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)

d.end()
