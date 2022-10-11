d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.low)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.position_pen(0,2)

d.end()
