d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.position_pen(3,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,0)
d.curve(Direction.N, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.NW, Length.short)

d.end()
