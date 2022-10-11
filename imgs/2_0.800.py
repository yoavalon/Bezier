d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)

d.end()
