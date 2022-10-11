d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)

d.end()
