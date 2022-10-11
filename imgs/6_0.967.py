d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)
d.position_pen(2,2)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)

d.end()
