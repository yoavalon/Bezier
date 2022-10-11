d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.N, Orient.right, Length.long, Radius.low)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)

d.end()
