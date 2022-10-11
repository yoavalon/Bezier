d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.position_pen(3,0)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(1,3)

d.end()
