d = DslBezier()

d.position_pen(3,1)
d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.position_pen(2,0)
d.position_pen(1,0)

d.end()
