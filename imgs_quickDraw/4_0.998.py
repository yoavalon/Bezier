d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,1)

d.end()
