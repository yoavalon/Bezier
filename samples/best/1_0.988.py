d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.position_pen(2,1)
d.position_pen(0,1)

d.end()
