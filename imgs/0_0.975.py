d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.short)

d.end()
