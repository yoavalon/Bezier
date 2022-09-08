d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(3,2)
d.position_pen(1,2)
d.position_pen(2,3)
d.position_pen(1,0)
d.position_pen(0,2)

d.end()
