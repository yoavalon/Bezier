d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.position_pen(3,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)

d.end()
