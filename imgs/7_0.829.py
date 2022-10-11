d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)

d.end()
