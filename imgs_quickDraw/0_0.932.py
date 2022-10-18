d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,2)

d.end()
