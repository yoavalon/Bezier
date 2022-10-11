d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.position_pen(1,2)
d.straight_line(Direction.N, Length.medium)

d.end()
