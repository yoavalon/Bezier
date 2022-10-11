d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,0)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,0)

d.end()
