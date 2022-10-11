d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.NE, Length.short)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)

d.end()
