d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
