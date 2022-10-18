d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
