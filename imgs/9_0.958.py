d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.N, Orient.left, Length.short, Radius.low)

d.end()
