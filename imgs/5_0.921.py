d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)

d.end()
