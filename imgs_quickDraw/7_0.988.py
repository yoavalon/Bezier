d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.N, Length.medium)
d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
