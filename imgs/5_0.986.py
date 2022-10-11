d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.long)

d.end()
