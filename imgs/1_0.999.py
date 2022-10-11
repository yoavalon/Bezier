d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)

d.end()
