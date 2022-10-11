d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)
d.position_pen(2,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)

d.end()
