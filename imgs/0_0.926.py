d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)

d.end()
