d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)
d.position_pen(2,2)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.E, Length.medium)

d.end()
