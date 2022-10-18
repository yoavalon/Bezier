d = DslBezier()

d.position_pen(0,1)
d.position_pen(3,2)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(3,1)

d.end()
