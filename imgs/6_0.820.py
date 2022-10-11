d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.position_pen(0,2)

d.end()
