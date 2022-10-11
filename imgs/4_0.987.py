d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.position_pen(3,2)

d.end()
