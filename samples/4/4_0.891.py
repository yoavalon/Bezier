d = DslBezier()

d.position_pen(1,3)
d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.position_pen(2,2)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)

d.end()
