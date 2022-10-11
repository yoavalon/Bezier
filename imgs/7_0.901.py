d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
