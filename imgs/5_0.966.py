d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.N, Length.medium)

d.end()
