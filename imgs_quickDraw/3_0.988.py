d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)

d.end()
