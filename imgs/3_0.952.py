d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)

d.end()
