d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)

d.end()
