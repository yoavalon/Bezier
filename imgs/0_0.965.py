d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)
d.position_pen(1,2)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.NE, Length.medium)

d.end()
