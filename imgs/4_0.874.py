d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.position_pen(0,2)

d.end()
