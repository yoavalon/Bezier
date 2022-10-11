d = DslBezier()

d.position_pen(2,3)
d.position_pen(2,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)

d.end()
