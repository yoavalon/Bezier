d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)

d.end()
