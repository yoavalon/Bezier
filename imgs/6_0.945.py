d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.position_pen(1,1)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)

d.end()
