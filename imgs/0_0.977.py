d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)

d.end()
