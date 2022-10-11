d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.position_pen(2,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)

d.end()
