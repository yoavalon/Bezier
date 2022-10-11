d = DslBezier()

d.position_pen(3,0)
d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)

d.end()
