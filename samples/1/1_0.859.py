d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)

d.end()
