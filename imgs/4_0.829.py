d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)

d.end()
