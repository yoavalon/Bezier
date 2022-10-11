d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.short)
d.position_pen(3,2)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.W, Length.medium)
d.position_pen(3,2)

d.end()
