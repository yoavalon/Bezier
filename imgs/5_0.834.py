d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.S, Length.short)

d.end()
