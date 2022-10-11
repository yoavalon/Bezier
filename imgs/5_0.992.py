d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.position_pen(0,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)

d.end()
