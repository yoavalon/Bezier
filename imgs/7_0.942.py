d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.NE, Length.medium)

d.end()
