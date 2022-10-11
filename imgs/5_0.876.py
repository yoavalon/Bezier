d = DslBezier()

d.position_pen(1,1)
d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.position_pen(1,0)

d.end()
