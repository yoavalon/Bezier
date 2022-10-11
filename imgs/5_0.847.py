d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.left, Length.short, Radius.high)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.SW, Length.medium)

d.end()
