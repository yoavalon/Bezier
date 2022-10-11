d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.position_pen(1,1)

d.end()
