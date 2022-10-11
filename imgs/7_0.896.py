d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,0)
d.straight_line(Direction.S, Length.medium)

d.end()
