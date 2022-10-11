d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)

d.end()
