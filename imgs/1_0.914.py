d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)

d.end()
