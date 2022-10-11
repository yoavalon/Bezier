d = DslBezier()

d.position_pen(3,2)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)
d.position_pen(3,2)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)

d.end()
