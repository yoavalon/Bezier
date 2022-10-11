d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)

d.end()
