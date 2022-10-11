d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.position_pen(2,2)

d.end()
