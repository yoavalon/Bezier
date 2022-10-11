d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.position_pen(3,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.position_pen(1,0)

d.end()
