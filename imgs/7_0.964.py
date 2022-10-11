d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.position_pen(2,1)

d.end()
