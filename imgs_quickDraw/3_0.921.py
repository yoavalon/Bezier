d = DslBezier()

d.position_pen(3,3)
d.position_pen(0,0)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(1,0)

d.end()
