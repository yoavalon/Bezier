d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.N, Orient.right, Length.long, Radius.high)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)

d.end()
