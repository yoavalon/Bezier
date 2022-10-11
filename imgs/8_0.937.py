d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)

d.end()
