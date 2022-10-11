d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.short, Radius.low)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)

d.end()
