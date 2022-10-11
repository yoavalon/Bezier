d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.position_pen(3,2)
d.position_pen(3,1)

d.end()
