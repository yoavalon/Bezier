d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.short)

d.end()
