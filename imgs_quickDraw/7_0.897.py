d = DslBezier()

d.position_pen(1,3)
d.position_pen(3,2)
d.curve(Direction.W, Orient.left, Length.short, Radius.low)

d.end()
