d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)

d.end()
