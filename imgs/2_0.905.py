d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.curve(Direction.E, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)

d.end()
