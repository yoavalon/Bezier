d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)
d.position_pen(3,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)

d.end()
