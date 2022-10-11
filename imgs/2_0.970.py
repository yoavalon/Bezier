d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)

d.end()
