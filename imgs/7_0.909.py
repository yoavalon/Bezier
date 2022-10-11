d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)
d.position_pen(2,3)

d.end()
