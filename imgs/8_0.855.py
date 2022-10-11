d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)

d.end()
