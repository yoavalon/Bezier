d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.position_pen(2,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)

d.end()
