d = DslBezier()

d.position_pen(1,0)
d.position_pen(0,1)
d.position_pen(2,3)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.position_pen(0,1)

d.end()
