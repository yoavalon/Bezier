d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.position_pen(1,2)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)

d.end()
