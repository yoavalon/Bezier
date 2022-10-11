d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SE, Length.short)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)

d.end()
