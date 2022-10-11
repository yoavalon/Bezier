d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.position_pen(1,3)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.position_pen(0,1)

d.end()
