d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.position_pen(2,1)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.long, Radius.high)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)

d.end()
