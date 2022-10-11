d = DslBezier()

d.position_pen(1,3)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.position_pen(1,1)

d.end()
