d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.position_pen(0,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)

d.end()
