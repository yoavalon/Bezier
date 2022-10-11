d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)

d.end()
