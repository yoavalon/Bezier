d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(0,1)

d.end()
