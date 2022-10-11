d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)

d.end()
