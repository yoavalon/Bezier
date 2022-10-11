d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)

d.end()
