d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.S, Length.short)

d.end()
