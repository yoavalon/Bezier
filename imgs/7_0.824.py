d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)

d.end()
