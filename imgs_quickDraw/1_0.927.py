d = DslBezier()

d.position_pen(2,3)
d.position_pen(0,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)

d.end()
