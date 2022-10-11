d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.position_pen(3,0)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.short)

d.end()
