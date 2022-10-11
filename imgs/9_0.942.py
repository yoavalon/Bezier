d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)
d.position_pen(2,2)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)

d.end()
