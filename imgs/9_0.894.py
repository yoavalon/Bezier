d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)

d.end()
