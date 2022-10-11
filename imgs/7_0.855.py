d = DslBezier()

d.position_pen(1,2)
d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(1,2)

d.end()
