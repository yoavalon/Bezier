d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.short)

d.end()
