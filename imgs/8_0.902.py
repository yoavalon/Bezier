d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.W, Length.medium)

d.end()
