d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.position_pen(2,0)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SE, Length.short)

d.end()
