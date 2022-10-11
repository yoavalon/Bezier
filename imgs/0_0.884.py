d = DslBezier()

d.position_pen(2,1)
d.position_pen(0,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)

d.end()
