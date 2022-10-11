d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)

d.end()
