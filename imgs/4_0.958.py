d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.long)

d.end()
