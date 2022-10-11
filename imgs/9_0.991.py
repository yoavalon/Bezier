d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.S, Length.medium)

d.end()
