d = DslBezier()

d.position_pen(3,0)
d.position_pen(0,0)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)

d.end()
