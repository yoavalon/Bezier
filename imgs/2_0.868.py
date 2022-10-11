d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)

d.end()
