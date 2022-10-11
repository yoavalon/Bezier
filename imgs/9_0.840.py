d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.position_pen(0,2)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)

d.end()
