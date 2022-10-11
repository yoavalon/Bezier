d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)

d.end()
