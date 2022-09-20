d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)
d.position_pen(0,2)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)

d.end()
