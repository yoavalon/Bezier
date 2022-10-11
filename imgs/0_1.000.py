d = DslBezier()

d.position_pen(0,2)
d.position_pen(2,2)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)

d.end()
