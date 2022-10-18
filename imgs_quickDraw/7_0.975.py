d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)

d.end()
