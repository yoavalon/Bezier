d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
