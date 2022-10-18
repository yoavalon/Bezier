d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.curve(Direction.E, Orient.right, Length.short, Radius.low)
d.position_pen(3,2)
d.straight_line(Direction.W, Length.short)

d.end()
