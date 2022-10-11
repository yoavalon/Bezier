d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(0,1)

d.end()
