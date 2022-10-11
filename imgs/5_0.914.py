d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(0,0)

d.end()
