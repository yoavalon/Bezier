d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.SW, Length.long)

d.end()
