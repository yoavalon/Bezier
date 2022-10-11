d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.position_pen(1,2)

d.end()
