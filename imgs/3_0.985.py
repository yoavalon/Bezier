d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)

d.end()
