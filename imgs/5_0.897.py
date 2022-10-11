d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.W, Length.long)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.medium)

d.end()
