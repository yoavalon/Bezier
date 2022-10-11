d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.W, Length.short)

d.end()
