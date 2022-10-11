d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.N, Orient.right, Length.long, Radius.low)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)

d.end()
