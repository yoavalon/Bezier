d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(0,2)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)

d.end()
