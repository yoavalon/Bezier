d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.SW, Length.long)

d.end()
