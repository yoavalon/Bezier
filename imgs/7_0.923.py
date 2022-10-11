d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)

d.end()
