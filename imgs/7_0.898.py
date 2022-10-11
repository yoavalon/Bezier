d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)

d.end()
