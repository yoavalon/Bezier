d = DslBezier()

d.position_pen(0,3)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.position_pen(2,0)
d.curve(Direction.N, Orient.left, Length.short, Radius.high)

d.end()
