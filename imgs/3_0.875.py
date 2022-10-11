d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
