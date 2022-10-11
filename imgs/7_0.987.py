d = DslBezier()

d.position_pen(0,0)
d.position_pen(0,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.position_pen(1,0)

d.end()
