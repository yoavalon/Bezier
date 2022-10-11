d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)

d.end()
