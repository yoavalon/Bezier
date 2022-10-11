d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)

d.end()
