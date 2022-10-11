d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.N, Length.medium)
d.position_pen(0,3)
d.straight_line(Direction.W, Length.short)

d.end()
