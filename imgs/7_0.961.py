d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.position_pen(3,1)

d.end()
