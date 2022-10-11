d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)
d.position_pen(2,1)

d.end()
