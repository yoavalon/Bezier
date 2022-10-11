d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)

d.end()
