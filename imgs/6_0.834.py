d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.S, Length.short)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NE, Length.long)
d.position_pen(2,0)

d.end()
