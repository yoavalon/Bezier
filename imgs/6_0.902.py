d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.position_pen(2,1)

d.end()
