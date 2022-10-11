d = DslBezier()

d.position_pen(2,3)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.position_pen(3,0)

d.end()
