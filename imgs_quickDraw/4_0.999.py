d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,1)
d.position_pen(0,2)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.high)

d.end()
