d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.NE, Length.long)
d.position_pen(3,3)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)

d.end()
