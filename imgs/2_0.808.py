d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.N, Orient.left, Length.short, Radius.high)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)

d.end()
