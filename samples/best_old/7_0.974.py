d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.position_pen(1,3)
d.position_pen(2,2)
d.position_pen(0,1)
d.position_pen(3,2)

d.end()
