d = DslBezier()

d.position_pen(1,2)
d.position_pen(3,2)
d.position_pen(1,1)
d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)

d.end()
