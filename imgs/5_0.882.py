d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SE, Length.medium)

d.end()
