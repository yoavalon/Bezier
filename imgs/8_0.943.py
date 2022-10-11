d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.position_pen(2,3)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)

d.end()
