d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.position_pen(1,0)
d.position_pen(2,3)

d.end()
