d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)

d.end()
