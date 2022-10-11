d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)

d.end()
