d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)

d.end()
