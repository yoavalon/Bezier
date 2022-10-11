d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.position_pen(0,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)

d.end()
