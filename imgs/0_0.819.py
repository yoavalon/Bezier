d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.curve(Direction.W, Orient.right, Length.long, Radius.high)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(3,1)

d.end()
