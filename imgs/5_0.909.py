d = DslBezier()

d.position_pen(0,3)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,3)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)

d.end()
