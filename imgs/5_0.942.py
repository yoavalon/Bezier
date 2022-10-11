d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)

d.end()
