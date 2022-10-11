d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.low)

d.end()
