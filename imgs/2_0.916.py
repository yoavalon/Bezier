d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.low)
d.position_pen(0,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)

d.end()
