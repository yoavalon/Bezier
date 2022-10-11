d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)

d.end()
