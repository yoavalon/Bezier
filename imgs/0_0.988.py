d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.position_pen(3,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)

d.end()
