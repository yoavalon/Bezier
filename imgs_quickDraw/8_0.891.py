d = DslBezier()

d.position_pen(0,3)
d.position_pen(1,3)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.W, Length.long)

d.end()
