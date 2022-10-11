d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)

d.end()
