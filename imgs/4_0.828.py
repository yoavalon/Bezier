d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.short, Radius.low)
d.position_pen(1,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,1)

d.end()
