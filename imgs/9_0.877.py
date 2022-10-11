d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.N, Length.medium)

d.end()
