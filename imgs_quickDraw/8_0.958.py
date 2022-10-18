d = DslBezier()

d.position_pen(3,2)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.E, Length.medium)

d.end()
