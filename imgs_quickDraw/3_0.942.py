d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.position_pen(3,1)

d.end()
