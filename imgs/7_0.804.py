d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.W, Length.medium)

d.end()
