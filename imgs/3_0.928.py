d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,3)

d.end()
