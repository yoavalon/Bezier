d = DslBezier()

d.position_pen(2,1)
d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.position_pen(3,2)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.position_pen(2,2)

d.end()
