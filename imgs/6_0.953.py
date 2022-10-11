d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.N, Length.medium)

d.end()
