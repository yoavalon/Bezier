d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,1)

d.end()
