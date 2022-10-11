d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.NW, Orient.right, Length.short, Radius.medium)
d.position_pen(3,1)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)

d.end()
