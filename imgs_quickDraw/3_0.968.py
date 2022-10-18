d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.W, Orient.left, Length.short, Radius.low)

d.end()
