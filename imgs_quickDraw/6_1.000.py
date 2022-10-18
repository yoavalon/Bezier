d = DslBezier()

d.position_pen(1,1)
d.position_pen(0,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)

d.end()
