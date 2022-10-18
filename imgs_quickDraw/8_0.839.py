d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.position_pen(2,0)

d.end()
