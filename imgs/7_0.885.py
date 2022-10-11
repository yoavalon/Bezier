d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.position_pen(3,3)
d.position_pen(1,2)

d.end()
