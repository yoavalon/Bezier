d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.N, Orient.left, Length.long, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(2,0)
d.position_pen(1,0)

d.end()
