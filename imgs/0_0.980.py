d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)

d.end()
