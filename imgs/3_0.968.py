d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.N, Orient.left, Length.short, Radius.high)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)

d.end()
