d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)

d.end()
