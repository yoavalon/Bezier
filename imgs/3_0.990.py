d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)

d.end()
