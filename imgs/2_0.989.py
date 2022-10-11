d = DslBezier()

d.position_pen(2,1)
d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)

d.end()
