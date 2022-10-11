d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)

d.end()
