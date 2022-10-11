d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)

d.end()
