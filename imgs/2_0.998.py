d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.position_pen(1,3)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.position_pen(0,2)

d.end()
