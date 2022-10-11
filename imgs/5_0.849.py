d = DslBezier()

d.position_pen(1,1)
d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(3,2)

d.end()
