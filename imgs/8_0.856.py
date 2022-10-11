d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.NE, Length.short)

d.end()
