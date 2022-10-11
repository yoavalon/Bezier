d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.NE, Length.short)
d.position_pen(0,2)
d.position_pen(2,2)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.medium)

d.end()
