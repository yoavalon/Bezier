d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.long, Radius.high)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.S, Length.long)
d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)

d.end()
