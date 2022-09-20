d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.position_pen(2,1)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)

d.end()
