d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)

d.end()
