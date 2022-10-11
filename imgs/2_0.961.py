d = DslBezier()

d.position_pen(1,1)
d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)

d.end()
