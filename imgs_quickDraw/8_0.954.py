d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.position_pen(3,1)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)

d.end()
