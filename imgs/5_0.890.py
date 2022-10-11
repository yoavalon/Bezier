d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)
d.position_pen(2,2)

d.end()
