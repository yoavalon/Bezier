d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(3,2)

d.end()
