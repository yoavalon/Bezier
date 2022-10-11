d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.SE, Length.long)
d.position_pen(1,2)
d.straight_line(Direction.NW, Length.medium)

d.end()
