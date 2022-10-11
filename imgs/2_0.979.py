d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.low)
d.position_pen(0,1)

d.end()
