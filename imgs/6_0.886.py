d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)

d.end()
