d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(1,1)

d.end()
