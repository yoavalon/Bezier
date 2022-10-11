d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(2,3)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,1)

d.end()
